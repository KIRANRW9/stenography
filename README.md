# 🔒 Advanced Steganography Tool

A modern, interactive Python application for hiding and revealing secret messages within images using LSB (Least Significant Bit) steganography technique.

![App Interface](https://github.com/KIRANRW9/stenography/blob/repo-exercise/screenshots/decrypt-tab.png)

## ✨ Features

- **🎨 Modern Dark UI** - Professional tabbed interface with intuitive design
- **🖼️ Image Preview** - Real-time thumbnails of selected images
- **📝 Interactive Text Areas** - Scrollable message input with character counter
- **🔐 Password Protection** - Secure encryption/decryption with password verification
- **⚡ Progress Indicators** - Visual feedback during operations
- **📊 Status Updates** - Real-time status bar showing current operations
- **🗂️ Multiple Formats** - Support for PNG, JPG, and JPEG image formats
- **💾 Smart File Management** - Timestamped saves and quick access to recent files

## 🖥️ Screenshots

### Encryption Interface
![Encryption Tab](https://github.com/KIRANRW9/stenography/blob/repo-exercise/screenshots/encrypt-tab.png)
*Hide secret messages in cover images with password protection*

### Decryption Interface
![Decryption Tab](https://github.com/KIRANRW9/stenography/blob/repo-exercise/screenshots/decrypt-tab.png)
*Reveal hidden messages from encrypted images*

### Information Guide
![Information Tab](https://github.com/KIRANRW9/stenography/blob/repo-exercise/screenshots/info-tab.png)
*Complete usage guide and steganography information*

### Original vs Encrypted Comparison
![Original Image](https://github.com/KIRANRW9/stenography/blob/repo-exercise/screenshots/original-image.png)
*Original cover image - beautiful ship blueprint design*

![Encrypted Image](https://github.com/KIRANRW9/stenography/blob/repo-exercise/screenshots/encrypted-image.png)
*Encrypted image with hidden message - visually identical but contains secret data*

> **Note**: Both images appear identical to the human eye, demonstrating the effectiveness of LSB steganography!

## 🚀 Quick Start

### Prerequisites
- Python 3.6 or higher
- Required libraries (see installation)

### Installation

```bash
# Clone the repository
git clone https://github.com/KIRANRW9/stenography.git
cd stenography

# Install required dependencies
pip install opencv-python pillow

# Run the application
python steganography_app.py
```

### Usage

#### 🔐 Encrypting a Message
1. Open the **Encrypt Message** tab
2. Click **"🖼️ Select Cover Image"** and choose your image
3. Enter your secret message in the text area
4. Set a secure password
5. Click **"🔐 Encrypt & Hide Message"**
6. Save the generated encrypted image

#### 🔓 Decrypting a Message
1. Open the **Decrypt Message** tab
2. Click **"📁 Select Encrypted Image"** or **"🔄 Use Last Encrypted"**
3. Enter the decryption password
4. Click **"🔓 Decrypt & Reveal Message"**
5. View your hidden message in the result area

## 🛠️ Technical Details

### How It Works
- **LSB Steganography**: Modifies the least significant bit of each color channel
- **Binary Encoding**: Converts text to binary and embeds in image pixels
- **Delimiter System**: Uses unique binary pattern to mark message end
- **Password Verification**: Simple password matching for access control

### Supported Formats
- **Input**: PNG, JPG, JPEG
- **Output**: PNG (recommended for quality preservation)

### Capacity
Message capacity depends on image size:
- **Formula**: `(width × height × 3) ÷ 8 - 2` characters
- **Example**: 1920×1080 image ≈ 777,598 characters

## 📋 Requirements

```
opencv-python>=4.5.0
pillow>=8.0.0
tkinter (included with Python)
```

## 🔒 Security Notes

⚠️ **Important Security Considerations**:
- This tool provides **basic steganography** for educational purposes
- For sensitive data, combine with additional encryption methods
- Passwords are stored in plain text - use strong, unique passwords
- **Lost passwords cannot be recovered**
- PNG format preserves hidden data better than JPG

## 🎯 Use Cases

- **Educational**: Learn steganography concepts
- **Privacy**: Hide personal notes in images
- **Communication**: Covert message transmission
- **Digital Watermarking**: Embed metadata in images
- **Security Research**: Test steganographic detection

## 🤝 Contributing

Contributions are welcome! Here are some ways to contribute:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** your changes (`git commit -m 'Add some AmazingFeature'`)
4. **Push** to the branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request

### Enhancement Ideas
- [ ] Advanced encryption algorithms (AES, RSA)
- [ ] Batch processing for multiple images
- [ ] Detection resistance techniques
- [ ] Audio steganography support
- [ ] Web interface version
- [ ] Mobile app development

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **OpenCV** - Computer vision and image processing
- **Pillow** - Python imaging library
- **Tkinter** - GUI framework
- Ship blueprint image - Sample cover image for demonstrations

### Connect with Me
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/kiranrangu)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/KIRANRW9)
[![Email](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:kiranrw09@gmail.com)

---

## 📞 Contact & Support

### For Project-Related Inquiries:
- 📧 **Email**: kiranrw09@gmail.com
- 💼 **LinkedIn**: [linkedin.com/in/kiranrangu](https://www.linkedin.com/in/kiranrangu)
- 🐛 **Issues**: Please use GitHub Issues for bug reports and feature requests


---

<div align="center">

**⭐ Star this repository if you found it helpful!**

[Report Bug](../../issues) • [Request Feature](../../issues) • [Documentation](../../wiki)

</div>
