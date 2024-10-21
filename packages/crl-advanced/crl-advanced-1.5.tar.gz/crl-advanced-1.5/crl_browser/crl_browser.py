import sys
import subprocess
import os
import pty
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QLineEdit, QPushButton, QWidget,
    QHBoxLayout, QTabWidget, QMessageBox, QDialog, QLabel, QPlainTextEdit, QCheckBox
)
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWebEngineCore import QWebEngineUrlRequestInterceptor
from PyQt6.QtCore import QUrl, QObject, pyqtSignal, QThread, Qt
from PyQt6.QtGui import QKeyEvent
import re

class TorProxyDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Tor Proxy Settings")
        self.setFixedSize(400, 200)

        # Main layout
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Tor Proxy settings
        self.tor_proxy_label = QLabel("Enter Tor Proxy Address:")
        layout.addWidget(self.tor_proxy_label)

        # User input field
        self.tor_proxy_input = QLineEdit()
        self.tor_proxy_input.setPlaceholderText("e.g., socks5://127.0.0.1:9050")
        layout.addWidget(self.tor_proxy_input)

        # Save button
        save_button = QPushButton("Save")
        save_button.clicked.connect(self.save_settings)
        layout.addWidget(save_button)

    def save_settings(self):
        proxy_address = self.tor_proxy_input.text().strip()
        if proxy_address:
            QMessageBox.information(self, "Settings Saved", f"Tor Proxy set to: {proxy_address}")
            self.accept()
        else:
            QMessageBox.warning(self, "Input Error", "Please enter a valid proxy address.")

class AdBlocker(QWebEngineUrlRequestInterceptor):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Define ad/tracking patterns
        self.blocked_patterns = [
            re.compile(r".*ads\..*"),
            re.compile(r".*doubleclick\..*"),
            re.compile(r".*googlesyndication\..*"),
            re.compile(r".*google-analytics\..*"),
            re.compile(r".*tracking\..*"),
            re.compile(r".*adservice\..*"),
            re.compile(r".*facebook\..*"),
            re.compile(r".*youtube\..*"),
            re.compile(r".*twitter\..*"),
            re.compile(r".*linkedin\..*"),
            # Add more patterns as needed
        ]

    def interceptRequest(self, info):
        url = info.requestUrl().toString()
        for pattern in self.blocked_patterns:
            if pattern.match(url):
                info.block(True)
                # Optional: Log blocked URLs
                # print(f"Blocked: {url}")
                return

class SSHWorker(QObject):
    output_received = pyqtSignal(str)
    error_received = pyqtSignal(str)
    session_started = pyqtSignal()
    session_ended = pyqtSignal()

    def __init__(self, command):
        super().__init__()
        self.command = command
        self._running = True
        self.process = None
        self.master_fd = None

    def run(self):
        try:
            # Open a new pseudo-terminal
            self.master_fd, slave_fd = pty.openpty()
            # Start the SSH process
            self.process = subprocess.Popen(
                self.command,
                shell=True,
                stdin=slave_fd,
                stdout=slave_fd,
                stderr=slave_fd,
                universal_newlines=True,
                bufsize=0
            )
            self.session_started.emit()
            os.close(slave_fd)

            while self._running:
                try:
                    data = os.read(self.master_fd, 1024).decode()
                    if data:
                        self.output_received.emit(data)
                    else:
                        break
                except OSError:
                    break

            self.process.wait()
            self.session_ended.emit()
        except Exception as e:
            self.error_received.emit(str(e))

    def send_input(self, input_text):
        if self.master_fd:
            try:
                os.write(self.master_fd, (input_text + "\n").encode())
            except Exception as e:
                self.error_received.emit(str(e))

    def stop(self):
        self._running = False
        if self.process:
            self.process.terminate()

class TerminalTab(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)

        # Terminal output area
        self.terminal_output = QPlainTextEdit()
        self.terminal_output.setReadOnly(True)
        self.terminal_output.setStyleSheet("""
            QPlainTextEdit {
                background-color: #1e1e1e;
                color: #00ff00;
                font-family: Consolas, monospace;
                font-size: 12pt;
            }
        """)
        self.layout.addWidget(self.terminal_output)

        # Terminal input area
        self.terminal_input = QPlainTextEdit()
        self.terminal_input.setFixedHeight(50)
        self.terminal_input.setStyleSheet("""
            QPlainTextEdit {
                background-color: #2e2e2e;
                color: #ffffff;
                font-family: Consolas, monospace;
                font-size: 12pt;
            }
        """)
        self.terminal_input.installEventFilter(self)
        self.layout.addWidget(self.terminal_input)

        # Connect button
        connect_button = QPushButton("Connect via SSH")
        connect_button.clicked.connect(self.connect_to_ssh)
        self.layout.addWidget(connect_button)

        # SSHWorker and QThread
        self.worker = None
        self.thread = None

    def connect_to_ssh(self):
        ssh_command = self.terminal_input.toPlainText().strip()
        if ssh_command.startswith("ssh:"):
            ssh_command = ssh_command[4:].strip()  # Remove 'ssh:' prefix
            if "@" in ssh_command:
                username, ip_address = ssh_command.split("@", 1)
                if ip_address:
                    # Display connecting message
                    self.terminal_output.appendPlainText(f"Connecting to {username}@{ip_address}...\n")

                    # Start SSH session
                    self.start_ssh_session(username, ip_address)
                else:
                    QMessageBox.warning(self, "Input Error", "Please enter a valid IP address.")
            else:
                QMessageBox.warning(self, "Input Error", "Please include a username in the format 'ssh:user@ip_address'.")
        else:
            QMessageBox.warning(self, "Input Error", "Command must start with 'ssh:'. Use 'ssh:user@ip_address'.")

    def start_ssh_session(self, username, ip_address):
        command = f"ssh -tt {username}@{ip_address}"
        self.terminal_output.appendPlainText(f"Executing: {command}\n")

        # Create SSHWorker and QThread
        self.worker = SSHWorker(command)
        self.thread = QThread()
        self.worker.moveToThread(self.thread)

        # Connect signals
        self.thread.started.connect(self.worker.run)
        self.worker.output_received.connect(self.append_output)
        self.worker.error_received.connect(self.append_error)
        self.worker.session_started.connect(lambda: self.terminal_output.appendPlainText("SSH session started.\n"))
        self.worker.session_ended.connect(lambda: self.terminal_output.appendPlainText("SSH session ended.\n"))
        self.worker.session_ended.connect(self.thread.quit)
        self.worker.session_ended.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)

        # Start the thread
        self.thread.start()

    def append_output(self, text):
        self.terminal_output.appendPlainText(text)

    def append_error(self, error):
        self.terminal_output.appendPlainText(f"Error: {error}\n")

    def eventFilter(self, source, event):
        if source == self.terminal_input and event.type() == event.Type.KeyPress:
            if event.key() in (Qt.Key.Key_Return, Qt.Key.Key_Enter):
                input_text = self.terminal_input.toPlainText().strip()
                self.send_input(input_text)
                return True  # Event handled
        return super().eventFilter(source, event)

    def send_input(self, input_text):
        if self.worker:
            self.worker.send_input(input_text)
            self.terminal_input.clear()

class CRLBrowser(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("CRL BROWSER")
        self.resize(1920, 1080)

        # Main widget and layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)

        # Toolbar layout
        self.toolbar = QHBoxLayout()
        self.toolbar.setContentsMargins(10, 10, 10, 10)
        self.toolbar.setSpacing(10)
        self.main_layout.addLayout(self.toolbar)

        # Settings button
        self.settings_button = QPushButton("⚙ Settings")
        self.settings_button.clicked.connect(self.open_settings_dialog)
        self.toolbar.addWidget(self.settings_button)

        # New tab button
        self.new_tab_button = QPushButton("+")
        self.new_tab_button.setToolTip("New Tab")
        self.new_tab_button.clicked.connect(self.add_new_tab)
        self.toolbar.addWidget(self.new_tab_button)

        # Back button
        self.back_button = QPushButton("←")
        self.back_button.setToolTip("Back")
        self.back_button.clicked.connect(self.go_back)
        self.toolbar.addWidget(self.back_button)

        # Forward button
        self.forward_button = QPushButton("→")
        self.forward_button.setToolTip("Forward")
        self.forward_button.clicked.connect(self.go_forward)
        self.toolbar.addWidget(self.forward_button)

        # Refresh button
        self.refresh_button = QPushButton("↻")
        self.refresh_button.setToolTip("Refresh")
        self.refresh_button.clicked.connect(self.refresh_page)
        self.toolbar.addWidget(self.refresh_button)

        # Search input
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Search .onion or enter address...")
        self.search_input.setFixedHeight(30)
        self.search_input.setStyleSheet("""
            QLineEdit {
                background-color: #1e1e1e;
                color: #00ffff;
                border: 1px solid #00ffff;
                border-radius: 5px;
                padding: 5px;
            }
            QLineEdit:focus {
                border: 2px solid #ff00ff;
            }
        """)
        self.search_input.returnPressed.connect(self.navigate_to_url)
        self.toolbar.addWidget(self.search_input, stretch=1)

        # Tab widget
        self.tab_widget = QTabWidget()
        self.main_layout.addWidget(self.tab_widget)

        # First tab with DuckDuckGo
        self.web_view = QWebEngineView()

        # Apply ad-blocker to the profile
        self.ad_blocker = AdBlocker()
        profile = self.web_view.page().profile()
        profile.setUrlRequestInterceptor(self.ad_blocker)

        self.web_view.setUrl(QUrl("https://duckduckgo.com"))  # DuckDuckGo
        self.tab_widget.addTab(self.web_view, "Web")

        # Terminal tab
        self.terminal_tab = TerminalTab()
        self.tab_widget.addTab(self.terminal_tab, "Terminal")

        # Set background style
        self.setStyleSheet("background-color: #151515; color: #ffffff;")

        # Dynamic HTML response on load failure
        self.web_view.loadFinished.connect(self.check_load_status)

    def open_settings_dialog(self):
        """Open the settings dialog with ad-block toggle and Tor proxy settings."""
        dialog = QDialog(self)
        dialog.setWindowTitle("Settings")
        dialog.setFixedSize(400, 300)

        layout = QVBoxLayout()
        dialog.setLayout(layout)

        # AdBlock toggle
        self.adblock_checkbox = QCheckBox("Enable Ad Blocking")
        self.adblock_checkbox.setChecked(True)  # Default to enabled
        self.adblock_checkbox.stateChanged.connect(self.toggle_adblock)
        layout.addWidget(self.adblock_checkbox)

        # Tor Proxy settings button
        tor_button = QPushButton("Tor Proxy Settings")
        tor_button.clicked.connect(self.open_tor_proxy_settings)
        layout.addWidget(tor_button)

        # Close button
        close_button = QPushButton("Close")
        close_button.clicked.connect(dialog.accept)
        layout.addWidget(close_button)

        dialog.exec()

    def toggle_adblock(self, state):
        """Enable or disable ad-blocking based on the checkbox state."""
        if state == Qt.CheckState.Checked.value:
            self.ad_blocker.blocked_patterns = [
                re.compile(r".*ads\..*"),
                re.compile(r".*doubleclick\..*"),
                re.compile(r".*googlesyndication\..*"),
                re.compile(r".*google-analytics\..*"),
                re.compile(r".*tracking\..*"),
                re.compile(r".*adservice\..*"),
                re.compile(r".*facebook\..*"),
                re.compile(r".*youtube\..*"),
                re.compile(r".*twitter\..*"),
                re.compile(r".*linkedin\..*"),
                # Add more patterns as needed
            ]
            # Re-apply the interceptor to all open web views
            for index in range(self.tab_widget.count()):
                widget = self.tab_widget.widget(index)
                if isinstance(widget, QWebEngineView):
                    profile = widget.page().profile()
                    profile.setUrlRequestInterceptor(self.ad_blocker)
        else:
            # Clear blocked patterns to disable ad-blocking
            self.ad_blocker.blocked_patterns = []
            # Re-apply the interceptor to all open web views
            for index in range(self.tab_widget.count()):
                widget = self.tab_widget.widget(index)
                if isinstance(widget, QWebEngineView):
                    profile = widget.page().profile()
                    profile.setUrlRequestInterceptor(self.ad_blocker)

    def open_tor_proxy_settings(self):
        """Open the Tor Proxy settings dialog."""
        dialog = TorProxyDialog(self)
        dialog.exec()

    def add_new_tab(self):
        """Add a new tab with DuckDuckGo and apply ad-blocker if enabled."""
        new_web_view = QWebEngineView()

        # Apply ad-blocker to the profile if enabled
        if self.adblock_checkbox.isChecked() if hasattr(self, 'adblock_checkbox') else True:
            new_ad_blocker = AdBlocker()
            new_ad_blocker.blocked_patterns = self.ad_blocker.blocked_patterns
            profile = new_web_view.page().profile()
            profile.setUrlRequestInterceptor(new_ad_blocker)

        new_web_view.setUrl(QUrl("https://duckduckgo.com"))  # DuckDuckGo
        self.tab_widget.addTab(new_web_view, f"Tab {self.tab_widget.count() + 1}")

    def navigate_to_url(self):
        """Navigate to the URL entered in the search input."""
        url_text = self.search_input.text().strip()
        if url_text.endswith(".onion"):
            # Use Tor proxy for .onion connections
            url_text = f"http://{url_text}"  # Add http for .onion
        elif not url_text.startswith(("http://", "https://")):
            url_text = "http://" + url_text
        current_index = self.tab_widget.currentIndex()
        current_widget = self.tab_widget.currentWidget()
        if isinstance(current_widget, QWebEngineView):
            current_widget.setUrl(QUrl(url_text))

    def check_load_status(self, success):
        """Check the status of the page load."""
        if not success:
            # Show error page
            self.show_error_page()

    def show_error_page(self):
        """Show a dynamic HTML error page."""
        error_html = """
        <html>
            <head>
                <title>Error</title>
                <style>
                    body {
                        background-color: #151515;
                        color: #ff0000;
                        font-family: Arial, sans-serif;
                        text-align: center;
                        margin-top: 50px;
                    }
                    h1 {
                        color: #ff0000;
                    }
                </style>
            </head>
            <body>
                <h1>Connection Error</h1>
                <p>The domain is not available or the connection timed out.</p>
                <p>Please check the address and try again.</p>
            </body>
        </html>
        """
        current_widget = self.tab_widget.currentWidget()
        if isinstance(current_widget, QWebEngineView):
            current_widget.setHtml(error_html)

    def show_ip_not_found_page(self):
        """Show a separate HTML page when IP address is not found."""
        ip_not_found_html = """
        <html>
            <head>
                <title>IP Not Found</title>
                <style>
                    body {
                        background-color: #151515;
                        color: #ff0000;
                        font-family: Arial, sans-serif;
                        text-align: center;
                        margin-top: 50px;
                    }
                    h1 {
                        color: #ff0000;
                    }
                </style>
            </head>
            <body>
                <h1>IP Address Not Found</h1>
                <p>The IP address you entered could not be found.</p>
                <p>Please check the address and try again.</p>
            </body>
        </html>
        """
        current_widget = self.tab_widget.currentWidget()
        if isinstance(current_widget, QWebEngineView):
            current_widget.setHtml(ip_not_found_html)

    def show_ip_timeout_page(self):
        """Show a separate HTML page when the IP address response is too long."""
        ip_timeout_html = """
        <html>
            <head>
                <title>Connection Timeout</title>
                <style>
                    body {
                        background-color: #151515;
                        color: #ff0000;
                        font-family: Arial, sans-serif;
                        text-align: center;
                        margin-top: 50px;
                    }
                    h1 {
                        color: #ff0000;
                    }
                </style>
            </head>
            <body>
                <h1>Connection Timeout</h1>
                <p>The response from the IP address took too long.</p>
                <p>Please try again later.</p>
            </body>
        </html>
        """
        current_widget = self.tab_widget.currentWidget()
        if isinstance(current_widget, QWebEngineView):
            current_widget.setHtml(ip_timeout_html)

    def go_back(self):
        """Navigate back in the web view."""
        current_widget = self.tab_widget.currentWidget()
        if isinstance(current_widget, QWebEngineView):
            current_widget.back()

    def go_forward(self):
        """Navigate forward in the web view."""
        current_widget = self.tab_widget.currentWidget()
        if isinstance(current_widget, QWebEngineView):
            current_widget.forward()

    def refresh_page(self):
        """Refresh the current page."""
        current_widget = self.tab_widget.currentWidget()
        if isinstance(current_widget, QWebEngineView):
            current_widget.reload()


def main():
    app = QApplication(sys.argv)  # sys.argv'yi geçiriyoruz
    window = CRLBrowser()
    window.show()
    app.exec()  # PyQt6'da exec_ yerine exec kullanılır

if __name__ == "__main__":
    main()