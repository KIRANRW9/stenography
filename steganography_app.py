import cv2
import os
import numpy as np
from tkinter import *
from tkinter import filedialog, messagebox, simpledialog, ttk
from tkinter.scrolledtext import ScrolledText
from PIL import Image, ImageTk
import time

class InteractiveSteganographyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🔒 Advanced Steganography App")
        self.root.geometry("900x700")
        self.root.configure(bg='#2c3e50')
        
        # Initialize variables
        self.message_var = StringVar()
        self.password_var = StringVar()
        self.image_path = None
        self.encrypted_image_path = None
        self.progress = None
        
        # Configure style
        self.setup_styles()
        self.create_ui()
        
    def setup_styles(self):
        """Setup custom styles for the application"""
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Configure custom styles
        self.style.configure('Title.TLabel', font=('Arial', 16, 'bold'), background='#2c3e50', foreground='#ecf0f1')
        self.style.configure('Subtitle.TLabel', font=('Arial', 10), background='#2c3e50', foreground='#bdc3c7')
        self.style.configure('Custom.TButton', font=('Arial', 10, 'bold'))
        self.style.configure('Success.TLabel', font=('Arial', 10), background='#27ae60', foreground='white')
        self.style.configure('Error.TLabel', font=('Arial', 10), background='#e74c3c', foreground='white')

    def create_ui(self):
        """Create the interactive user interface"""
        # Main title
        title_frame = Frame(self.root, bg='#2c3e50')
        title_frame.pack(pady=20)
        
        title_label = Label(title_frame, text="🔒 Advanced Steganography Tool", 
                           font=('Arial', 20, 'bold'), bg='#2c3e50', fg='#ecf0f1')
        title_label.pack()
        
        subtitle_label = Label(title_frame, text="Hide and reveal secret messages in images", 
                              font=('Arial', 12), bg='#2c3e50', fg='#bdc3c7')
        subtitle_label.pack()
        
        # Create notebook for tabs
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=BOTH, expand=True, padx=20, pady=10)
        
        # Encrypt tab
        self.encrypt_frame = Frame(self.notebook, bg='#34495e')
        self.notebook.add(self.encrypt_frame, text="🔐 Encrypt Message")
        self.create_encrypt_tab()
        
        # Decrypt tab
        self.decrypt_frame = Frame(self.notebook, bg='#34495e')
        self.notebook.add(self.decrypt_frame, text="🔓 Decrypt Message")
        self.create_decrypt_tab()
        
        # Info tab
        self.info_frame = Frame(self.notebook, bg='#34495e')
        self.notebook.add(self.info_frame, text="ℹ️ Information")
        self.create_info_tab()
        
        # Status bar
        self.create_status_bar()
        
    def create_encrypt_tab(self):
        """Create the encryption tab"""
        # Image selection frame
        img_frame = LabelFrame(self.encrypt_frame, text="📷 Image Selection", 
                              font=('Arial', 12, 'bold'), bg='#34495e', fg='#ecf0f1')
        img_frame.pack(fill=X, padx=20, pady=10)
        
        Button(img_frame, text="🖼️ Select Cover Image", command=self.select_image,
               font=('Arial', 10, 'bold'), bg='#3498db', fg='white', 
               activebackground='#2980b9', pady=5).pack(pady=10)
        
        self.selected_img_label = Label(img_frame, text="No image selected", 
                                       bg='#34495e', fg='#bdc3c7')
        self.selected_img_label.pack()
        
        # Image preview
        self.img_preview_label = Label(img_frame, bg='#34495e')
        self.img_preview_label.pack(pady=10)
        
        # Message frame
        msg_frame = LabelFrame(self.encrypt_frame, text="💬 Secret Message", 
                              font=('Arial', 12, 'bold'), bg='#34495e', fg='#ecf0f1')
        msg_frame.pack(fill=BOTH, expand=True, padx=20, pady=10)
        
        Label(msg_frame, text="Enter your secret message:", 
              bg='#34495e', fg='#ecf0f1', font=('Arial', 10)).pack(anchor=W, padx=10, pady=5)
        
        self.message_text = ScrolledText(msg_frame, height=6, font=('Consolas', 10),
                                        bg='#2c3e50', fg='#ecf0f1', insertbackground='white')
        self.message_text.pack(fill=BOTH, expand=True, padx=10, pady=5)
        
        # Character counter
        self.char_count_label = Label(msg_frame, text="Characters: 0", 
                                     bg='#34495e', fg='#bdc3c7')
        self.char_count_label.pack(anchor=E, padx=10, pady=2)
        
        self.message_text.bind('<KeyRelease>', self.update_char_count)
        
        # Password frame
        pass_frame = Frame(msg_frame, bg='#34495e')
        pass_frame.pack(fill=X, padx=10, pady=5)
        
        Label(pass_frame, text="🔑 Password:", bg='#34495e', fg='#ecf0f1', 
              font=('Arial', 10)).pack(side=LEFT)
        
        self.password_entry = Entry(pass_frame, textvariable=self.password_var, show="*",
                                   font=('Arial', 10), bg='#2c3e50', fg='#ecf0f1', 
                                   insertbackground='white')
        self.password_entry.pack(side=LEFT, fill=X, expand=True, padx=(10, 0))
        
        # Encrypt button
        encrypt_btn = Button(msg_frame, text="🔐 Encrypt & Hide Message", 
                           command=self.encrypt_with_progress,
                           font=('Arial', 12, 'bold'), bg='#27ae60', fg='white',
                           activebackground='#229954', pady=10)
        encrypt_btn.pack(pady=20)
        
    def create_decrypt_tab(self):
        """Create the decryption tab"""
        # Image selection frame
        img_frame = LabelFrame(self.decrypt_frame, text="🖼️ Encrypted Image", 
                              font=('Arial', 12, 'bold'), bg='#34495e', fg='#ecf0f1')
        img_frame.pack(fill=X, padx=20, pady=10)
        
        btn_frame = Frame(img_frame, bg='#34495e')
        btn_frame.pack(pady=10)
        
        Button(btn_frame, text="📁 Select Encrypted Image", 
               command=self.select_encrypted_image,
               font=('Arial', 10, 'bold'), bg='#e67e22', fg='white',
               activebackground='#d35400', pady=5).pack(side=LEFT, padx=5)
        
        Button(btn_frame, text="🔄 Use Last Encrypted", 
               command=self.use_last_encrypted,
               font=('Arial', 10, 'bold'), bg='#9b59b6', fg='white',
               activebackground='#8e44ad', pady=5).pack(side=LEFT, padx=5)
        
        self.encrypted_img_label = Label(img_frame, text="No encrypted image selected", 
                                        bg='#34495e', fg='#bdc3c7')
        self.encrypted_img_label.pack()
        
        # Encrypted image preview
        self.encrypted_preview_label = Label(img_frame, bg='#34495e')
        self.encrypted_preview_label.pack(pady=10)
        
        # Decryption frame
        decrypt_frame = LabelFrame(self.decrypt_frame, text="🔓 Message Decryption", 
                                  font=('Arial', 12, 'bold'), bg='#34495e', fg='#ecf0f1')
        decrypt_frame.pack(fill=BOTH, expand=True, padx=20, pady=10)
        
        # Password frame
        pass_frame = Frame(decrypt_frame, bg='#34495e')
        pass_frame.pack(fill=X, padx=10, pady=10)
        
        Label(pass_frame, text="🔑 Password:", bg='#34495e', fg='#ecf0f1', 
              font=('Arial', 10)).pack(side=LEFT)
        
        self.decrypt_password_var = StringVar()
        self.decrypt_password_entry = Entry(pass_frame, textvariable=self.decrypt_password_var, 
                                           show="*", font=('Arial', 10), bg='#2c3e50', 
                                           fg='#ecf0f1', insertbackground='white')
        self.decrypt_password_entry.pack(side=LEFT, fill=X, expand=True, padx=(10, 0))
        
        # Decrypt button
        decrypt_btn = Button(decrypt_frame, text="🔓 Decrypt & Reveal Message", 
                           command=self.decrypt_with_progress,
                           font=('Arial', 12, 'bold'), bg='#e74c3c', fg='white',
                           activebackground='#c0392b', pady=10)
        decrypt_btn.pack(pady=20)
        
        # Result frame
        result_frame = LabelFrame(decrypt_frame, text="📝 Decrypted Message", 
                                 font=('Arial', 10, 'bold'), bg='#34495e', fg='#ecf0f1')
        result_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)
        
        self.result_text = ScrolledText(result_frame, height=8, font=('Consolas', 10),
                                       bg='#2c3e50', fg='#ecf0f1', insertbackground='white',
                                       state=DISABLED)
        self.result_text.pack(fill=BOTH, expand=True, padx=10, pady=10)
        
    def create_info_tab(self):
        """Create the information tab"""
        info_text = """
        🔒 STEGANOGRAPHY INFORMATION
        
        What is Steganography?
        Steganography is the practice of hiding secret information within ordinary files or images.
        Unlike cryptography, which scrambles data, steganography hides the very existence of the data.
        
        How this app works:
        • Uses LSB (Least Significant Bit) technique
        • Modifies the last bit of each color channel in image pixels
        • Changes are invisible to the human eye
        • Supports PNG, JPG, and JPEG image formats
        
        🔐 ENCRYPTION PROCESS:
        1. Select a cover image (PNG/JPG/JPEG)
        2. Enter your secret message
        3. Set a strong password
        4. Click "Encrypt & Hide Message"
        5. Save the generated encrypted image
        
        🔓 DECRYPTION PROCESS:
        1. Select the encrypted image
        2. Enter the correct password
        3. Click "Decrypt & Reveal Message"
        4. View your hidden message
        
        💡 TIPS:
        • Use high-resolution images for better capacity
        • Choose complex passwords for security
        • Keep the original encrypted image safe
        • PNG format preserves quality better than JPG
        
        ⚠️ SECURITY NOTES:
        • This tool provides basic steganography
        • For sensitive data, use additional encryption
        • Password is required for decryption
        • Lost passwords cannot be recovered
        """
        
        info_display = ScrolledText(self.info_frame, font=('Consolas', 10),
                                   bg='#2c3e50', fg='#ecf0f1', wrap=WORD,
                                   state=DISABLED)
        info_display.pack(fill=BOTH, expand=True, padx=20, pady=20)
        
        info_display.config(state=NORMAL)
        info_display.insert(1.0, info_text)
        info_display.config(state=DISABLED)
        
    def create_status_bar(self):
        """Create status bar at the bottom"""
        self.status_frame = Frame(self.root, bg='#1a252f', height=30)
        self.status_frame.pack(fill=X, side=BOTTOM)
        
        self.status_label = Label(self.status_frame, text="Ready", 
                                 bg='#1a252f', fg='#ecf0f1', font=('Arial', 9))
        self.status_label.pack(side=LEFT, padx=10, pady=5)
        
        self.progress_var = StringVar(value="")
        self.progress_label = Label(self.status_frame, textvariable=self.progress_var,
                                   bg='#1a252f', fg='#3498db', font=('Arial', 9))
        self.progress_label.pack(side=RIGHT, padx=10, pady=5)
        
    def update_status(self, message):
        """Update status bar message"""
        self.status_label.config(text=message)
        self.root.update_idletasks()
        
    def update_char_count(self, event=None):
        """Update character count for message"""
        count = len(self.message_text.get(1.0, END).strip())
        self.char_count_label.config(text=f"Characters: {count}")
        
    def load_and_preview_image(self, image_path, preview_label, max_size=(150, 150)):
        """Load and display image preview"""
        try:
            img = Image.open(image_path)
            img.thumbnail(max_size, Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(img)
            preview_label.config(image=photo)
            preview_label.image = photo  # Keep a reference
        except Exception as e:
            print(f"Error loading preview: {e}")
            
    def select_image(self):
        """Select cover image for encryption"""
        self.image_path = filedialog.askopenfilename(
            title="Select Cover Image", 
            filetypes=[("Image files", "*.png *.jpg *.jpeg *.PNG *.JPG *.JPEG")]
        )
        if self.image_path:
            filename = os.path.basename(self.image_path)
            self.selected_img_label.config(text=f"Selected: {filename}")
            self.load_and_preview_image(self.image_path, self.img_preview_label)
            self.update_status(f"Cover image selected: {filename}")
        else:
            self.update_status("No image selected")
            
    def select_encrypted_image(self):
        """Select encrypted image for decryption"""
        self.encrypted_image_path = filedialog.askopenfilename(
            title="Select Encrypted Image", 
            filetypes=[("Image files", "*.png *.jpg *.jpeg *.PNG *.JPG *.JPEG")]
        )
        if self.encrypted_image_path:
            filename = os.path.basename(self.encrypted_image_path)
            self.encrypted_img_label.config(text=f"Selected: {filename}")
            self.load_and_preview_image(self.encrypted_image_path, self.encrypted_preview_label)
            self.update_status(f"Encrypted image selected: {filename}")
            
    def use_last_encrypted(self):
        """Use the last encrypted image"""
        if os.path.exists("Encryptedmsg.png"):
            self.encrypted_image_path = "Encryptedmsg.png"
            self.encrypted_img_label.config(text="Selected: Encryptedmsg.png (Last encrypted)")
            self.load_and_preview_image(self.encrypted_image_path, self.encrypted_preview_label)
            self.update_status("Using last encrypted image")
        else:
            messagebox.showwarning("Warning", "No previous encrypted image found!")
            
    def create_progress_window(self, title, message):
        """Create a progress window"""
        progress_window = Toplevel(self.root)
        progress_window.title(title)
        progress_window.geometry("300x120")
        progress_window.configure(bg='#34495e')
        progress_window.resizable(False, False)
        
        # Center the window
        progress_window.transient(self.root)
        progress_window.grab_set()
        
        Label(progress_window, text=message, bg='#34495e', fg='#ecf0f1',
              font=('Arial', 10)).pack(pady=20)
        
        progress_bar = ttk.Progressbar(progress_window, mode='indeterminate')
        progress_bar.pack(pady=10, padx=20, fill=X)
        progress_bar.start()
        
        return progress_window, progress_bar
        
    def encrypt_with_progress(self):
        """Encrypt with progress indication"""
        if not self.image_path:
            messagebox.showerror("Error", "Please select a cover image first!")
            return
            
        message = self.message_text.get(1.0, END).strip()
        password = self.password_var.get()
        
        if not message:
            messagebox.showerror("Error", "Please enter a secret message!")
            return
            
        if not password:
            messagebox.showerror("Error", "Please enter a password!")
            return
            
        if len(password) < 4:
            messagebox.showwarning("Warning", "Consider using a stronger password (4+ characters)")
            
        # Create progress window
        progress_window, progress_bar = self.create_progress_window(
            "Encrypting", "Hiding message in image...")
        
        try:
            self.update_status("Loading image...")
            img = cv2.imread(self.image_path)
            
            if img is None:
                messagebox.showerror("Error", "Unable to load the selected image!")
                return
                
            # Check if message can fit in image
            max_chars = (img.shape[0] * img.shape[1] * img.shape[2]) // 8 - 2
            if len(message) > max_chars:
                messagebox.showerror("Error", f"Message too long! Maximum {max_chars} characters allowed.")
                return
                
            self.update_status("Encoding message...")
            encrypted_img = self.hide_text_in_image(img.copy(), message)
            
            # Save with timestamp
            timestamp = int(time.time())
            filename = f"Encryptedmsg_{timestamp}.png"
            
            self.update_status("Saving encrypted image...")
            cv2.imwrite("Encryptedmsg.png", encrypted_img)  # Default name
            cv2.imwrite(filename, encrypted_img)  # Timestamped version
            
            progress_window.destroy()
            
            # Success message with options
            result = messagebox.askyesno("Success!", 
                f"Message encrypted successfully!\n\nSaved as: {filename}\n\nWould you like to open the encrypted image?")
            
            if result:
                if os.name == 'nt':  # Windows
                    os.system(f"start {filename}")
                else:  # macOS and Linux
                    os.system(f"open {filename}")
                    
            self.update_status(f"Encryption completed - {filename}")
            
        except Exception as e:
            progress_window.destroy()
            messagebox.showerror("Error", f"Encryption failed: {str(e)}")
            self.update_status("Encryption failed")
            
    def decrypt_with_progress(self):
        """Decrypt with progress indication"""
        if not self.encrypted_image_path:
            messagebox.showerror("Error", "Please select an encrypted image first!")
            return
            
        password = self.decrypt_password_var.get()
        if not password:
            messagebox.showerror("Error", "Please enter the decryption password!")
            return
            
        # Create progress window
        progress_window, progress_bar = self.create_progress_window(
            "Decrypting", "Extracting hidden message...")
        
        try:
            self.update_status("Loading encrypted image...")
            img = cv2.imread(self.encrypted_image_path)
            
            if img is None:
                messagebox.showerror("Error", "Unable to load the encrypted image!")
                return
                
            self.update_status("Extracting message...")
            decrypted_message = self.retrieve_text_from_image(img)
            
            if not decrypted_message:
                progress_window.destroy()
                messagebox.showerror("Error", "No hidden message found or image is corrupted!")
                return
                
            # Simple password verification (in real app, use proper hashing)
            entered_password = simpledialog.askstring("Password Verification", 
                                                     "Confirm your password:", show="*")
            
            progress_window.destroy()
            
            if password == entered_password:
                # Display decrypted message
                self.result_text.config(state=NORMAL)
                self.result_text.delete(1.0, END)
                self.result_text.insert(1.0, decrypted_message)
                self.result_text.config(state=DISABLED)
                
                # Switch to decrypt tab to show result
                self.notebook.select(1)
                
                messagebox.showinfo("Success!", "Message decrypted successfully!")
                self.update_status("Decryption successful")
            else:
                messagebox.showerror("Error", "Invalid password! Access denied.")
                self.update_status("Decryption failed - Invalid password")
                
        except Exception as e:
            progress_window.destroy()
            messagebox.showerror("Error", f"Decryption failed: {str(e)}")
            self.update_status("Decryption failed")
            
    def hide_text_in_image(self, img, text):
        """Hide text in image using LSB steganography"""
        binary_text = ''.join(format(ord(char), '08b') for char in text)
        binary_text += '1111111111111110'  # Delimiter
        
        data_index = 0
        
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                for k in range(img.shape[2]):
                    if data_index < len(binary_text):
                        # Modify LSB
                        pixel = img[i, j, k]
                        binary_pixel = format(pixel, '08b')[:-1] + binary_text[data_index]
                        img[i, j, k] = int(binary_pixel, 2)
                        data_index += 1
                    else:
                        return img
        return img
        
    def retrieve_text_from_image(self, img):
        """Retrieve hidden text from image"""
        binary_data = ''
        
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                for k in range(img.shape[2]):
                    binary_data += format(img[i, j, k], '08b')[-1]
                    
                    # Check for delimiter
                    if len(binary_data) >= 16 and binary_data[-16:] == '1111111111111110':
                        binary_data = binary_data[:-16]  # Remove delimiter
                        
                        # Convert binary to text
                        message = ''
                        for l in range(0, len(binary_data), 8):
                            if l + 8 <= len(binary_data):
                                byte = binary_data[l:l+8]
                                if len(byte) == 8:
                                    try:
                                        char = chr(int(byte, 2))
                                        message += char
                                    except ValueError:
                                        continue
                        return message
        return ""

if __name__ == "__main__":
    root = Tk()
    app = InteractiveSteganographyApp(root)
    root.mainloop()
