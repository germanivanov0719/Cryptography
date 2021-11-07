# PyQt5 requirements
from resources.show_keys_dialogue import show_keys_dialogue

# other libs


class connections:
    def __init__(self):
        # Create dialogues
        #
        # self.show_keys_dialogue.exec()
        # self.show_keys_dialogue.hide()
        pass

    def connect(self):
        self.generate_fe.clicked.connect(self.fgenerate_fe)
        self.generate_fd.clicked.connect(self.fgenerate_fd)

        # Dialogues
        self.show_keys_dialogue.close_show.clicked.connect(self.fclose_show)
        self.show_keys_dialogue.clear_show.clicked.connect(self.fclear_show)

        # Fernet Encrypt/Decrypt
        self.helpText_fe.hide()
        self.helpText_fd.hide()
        self.help_fe.clicked.connect(self.fhelp_fe)
        self.help_fd.clicked.connect(self.fhelp_fd)
        self.encrypt_fe.clicked.connect(self.fencrypt_fe)
        self.decrypt_fd.clicked.connect(self.fdecrypt_fd)
        self.save_fe.clicked.connect(self.fsave_fe)
        self.save_fd.clicked.connect(self.fsave_fd)

        # Copy
        self.copy_fe.clicked.connect(self.fcopy_fe)
        self.copy_fd.clicked.connect(self.fcopy_fd)
        self.copy_sha.clicked.connect(self.fcopy_sha)
        self.copy_md5.clicked.connect(self.fcopy_md5)

        # Paste
        self.paste_fe.clicked.connect(self.fpaste_fe)
        self.paste_fd.clicked.connect(self.fpaste_fd)
        self.paste_sha.clicked.connect(self.fpaste_sha)
        self.paste_md5.clicked.connect(self.fpaste_md5)
        self.paste1_comp.clicked.connect(self.fpaste1_comp)
        self.paste2_comp.clicked.connect(self.fpaste2_comp)

        # Sha hashing
        self.helpText_sha.hide()
        self.help_sha.clicked.connect(self.fhelp_sha)
        self.hash_sha.clicked.connect(self.fhash_sha)
        self.file_sha.clicked.connect(self.ffile_sha)

        # Md5 hashing
        self.helpText_md5.hide()
        self.help_md5.clicked.connect(self.fhelp_md5)
        self.hash_md5.clicked.connect(self.fhash_md5)
        self.file_md5.clicked.connect(self.ffile_md5)

        # Compare
        self.textEdit1_comp.textChanged.connect(self.compare)
        self.textEdit2_comp.textChanged.connect(self.compare)

        # menubar
        self.menuEnglish.triggered.connect(self.to_english)
        self.menuRussian.triggered.connect(self.to_russian)
        self.show_keys_db.triggered.connect(self.fshow_keys_db)
