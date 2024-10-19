import sys
import io
import sounddevice as sd
import numpy as np
import requests
import json
import os
import base64
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QDialog, QTextEdit
from PySide6.QtCore import Qt, QPoint, QSize, QTimer, QBuffer, QByteArray, QIODevice
from PySide6.QtGui import QIcon, QMouseEvent, QFont, QColor, QClipboard, QPixmap, QScreen
import soundfile as sf
import anthropic


class ModernWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.dp, self.r, self.ad, self.sr, self.st = QPoint(), 0, [], 44100, None
        self.screen_capture = None
        self.transcription = ""
        self.initUI()

    def initUI(self):
        self.setStyleSheet(
            """
            QWidget#mainWidget {
                background-color: #f0f0f0;
                border-radius: 20px;
            }
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                padding: 10px 20px;
                text-align: center;
                text-decoration: none;
                font-size: 16px;
                margin: 4px 2px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            """
        )

        main_widget = QWidget(self)
        main_widget.setObjectName("mainWidget")
        main_layout = QHBoxLayout(main_widget)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(20)

        left_layout = QVBoxLayout()
        right_layout = QVBoxLayout()

        # Left side
        self.screen_view = QLabel()
        self.screen_view.setFixedSize(320, 180)  # 16:9 aspect ratio
        self.screen_view.setStyleSheet("border: 1px solid #999; border-radius: 10px;")
        left_layout.addWidget(self.screen_view)

        self.status_label = QLabel("Ready to record")
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.status_label.setStyleSheet("color: #666;")
        self.status_label.setWordWrap(True)
        left_layout.addWidget(self.status_label)

        left_layout.addStretch(1)

        # Right side
        title_label = QLabel("Swamix Copilot")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setStyleSheet("font-size: 24px; font-weight: bold; color: #333;")
        right_layout.addWidget(title_label)

        button_layout = QVBoxLayout()
        self.rb = QPushButton("Record Audio")
        self.rb.setIcon(QIcon("microphone_icon.jpg"))
        self.rb.setIconSize(QSize(24, 24))
        self.rb.clicked.connect(self.tr)
        button_layout.addWidget(self.rb)

        self.capture_button = QPushButton("Capture Screen")
        self.capture_button.clicked.connect(self.capture_screen)
        button_layout.addWidget(self.capture_button)

        self.send_button = QPushButton("Send to Claude")
        self.send_button.clicked.connect(self.send_to_claude)
        button_layout.addWidget(self.send_button)

        close_button = QPushButton("Close")
        close_button.setStyleSheet("background-color: #f44336;")
        close_button.clicked.connect(self.close)
        button_layout.addWidget(close_button)
        right_layout.addLayout(button_layout)
        right_layout.addStretch(1)

        main_layout.addLayout(left_layout, 2)
        main_layout.addLayout(right_layout, 1)

        outer_layout = QVBoxLayout(self)
        outer_layout.addWidget(main_widget)

        self.setMinimumSize(600, 400)
        self.resize(self.sizeHint())
        self.setWindowTitle('Modern Audio Recorder')
        self.show()

    def sizeHint(self):
        return QSize(600, 400)

    def tr(self):
        if not self.r:
            self.r = 1
            self.rb.setText("Stop Recording")
            self.rb.setStyleSheet("background-color: #f44336;")
            self.status_label.setText("Recording...")
            self.ad = []
            self.st = sd.InputStream(callback=self.ac, channels=1, samplerate=self.sr)
            self.st.start()
        else:
            self.r = 0
            self.rb.setText("Record Audio")
            self.rb.setStyleSheet("background-color: #4CAF50;")
            self.status_label.setText("Processing...")
            self.st and (self.st.stop(), self.st.close())
            self.pa()

    def ac(self, i, f, t, st):
        st and print(st)
        self.r and self.ad.append(i.copy())

    def pa(self):
        if not self.ad:
            self.status_label.setText("No audio data recorded")
            return
        a = np.concatenate(self.ad, axis=0)
        ab = io.BytesIO()
        sf.write(ab, a, self.sr, format='wav')
        ab.seek(0)
        self.ta(ab)

    def ta(self, af):
        self.status_label.setText("Transcribing...")
        u = "https://api.groq.com/openai/v1/audio/transcriptions"
        h = {"Authorization": f"Bearer {os.getenv('GROQ_API_KEY')}"}
        f = {"file": ("audio.wav", af, "audio/wav")}
        d = {"model": "whisper-large-v3", "temperature": 0, "response_format": "json", "language": "en"}
        r = requests.post(u, headers=h, files=f, data=d)
        result = r.json()['text'] if r.status_code == 200 else f"Error:{r.status_code} {r.text}"
        self.transcription = result  # Store the transcription
        self.status_label.setText(f"Transcription: {result}")
        print("Transcription:", result)
        QApplication.clipboard().setText(result)
        self.status_label.setText(f"Transcription copied to clipboard: {result}")

    def capture_screen(self):
        screen = QApplication.primaryScreen()
        self.screen_capture = screen.grabWindow(0)
        scaled_pixmap = self.screen_capture.scaled(self.screen_view.size(), Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        self.screen_view.setPixmap(scaled_pixmap)
        self.status_label.setText("Screen captured")

    def send_to_claude(self):
        if not self.screen_capture and not self.transcription:
            self.status_label.setText("provide either image or voiceover")
            return

        self.status_label.setText("Sending to Claude...")

        # Convert QPixmap to base64-encoded string
        buffer = QByteArray()
        buffer_io = QBuffer(buffer)
        buffer_io.open(QIODevice.OpenModeFlag.WriteOnly)
        self.screen_capture.save(buffer_io, "PNG")
        image_base64 = base64.b64encode(buffer.data()).decode('utf-8')

        # Create Anthropic client
        client = anthropic.Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))

        # Prepare the system prompt
        system_prompt = f"""
        # Task
        meme explainer, in simplified manner for 10th grader

        # Voice Transcript by user are
        {self.transcription}
        """

        try:
            response = client.messages.create(
                model="claude-3-sonnet-20240229",
                max_tokens=1024,
                temperature=0.7,
                system=system_prompt,
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "image",
                                "source": {
                                    "type": "base64",
                                    "media_type": "image/png",
                                    "data": image_base64,
                                },
                            },
                            {
                                "type": "text",
                                "text": f":please answer in a simplified 10th grader manner",
                            },
                        ],
                    }
                ],
            )

            self.status_label.setText("Response received from Claude")
            claude_response = response.content[0].text
            self.show_claude_response(claude_response)

            # Copy the response to clipboard
            QApplication.clipboard().setText(claude_response)
            self.status_label.setText("Response received and copied to clipboard")
        except Exception as e:
            self.status_label.setText(f"Error: {str(e)}")

    def show_claude_response(self, response):
        dialog = QDialog(self)
        dialog.setWindowTitle("Claude's Response")
        layout = QVBoxLayout(dialog)

        text_edit = QTextEdit()
        text_edit.setPlainText(response)
        text_edit.setReadOnly(True)
        layout.addWidget(text_edit)

        copy_button = QPushButton("Copy to Clipboard")
        copy_button.clicked.connect(lambda: self.copy_to_clipboard(response))
        layout.addWidget(copy_button)

        close_button = QPushButton("Close")
        close_button.clicked.connect(dialog.close)
        layout.addWidget(close_button)

        dialog.setLayout(layout)
        dialog.resize(500, 400)
        dialog.exec()

    def copy_to_clipboard(self, text):
        QApplication.clipboard().setText(text)
        self.status_label.setText("Response copied to clipboard")

    def mousePressEvent(self, e: QMouseEvent):
        if e.button() == Qt.MouseButton.LeftButton:
            self.dp = e.globalPosition().toPoint() - self.frameGeometry().topLeft()
            e.accept()

    def mouseMoveEvent(self, e: QMouseEvent):
        if e.buttons() & Qt.MouseButton.LeftButton:
            self.move(e.globalPosition().toPoint() - self.dp)
            e.accept()

    def mouseReleaseEvent(self, e: QMouseEvent):
        self.dp = QPoint()
        e.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ModernWidget()
    sys.exit(app.exec())
