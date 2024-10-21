import subprocess
import platform
import locale

class WindowsMailRetriever:
    def __init__(self):
        self.language_terms = {
            'en_US': {
                'wifi_interface': 'Wi-Fi',
                'wifi_profiles': 'All User Profiles',
                'owner': 'Registered Owner'
            },
            'it_IT': {
                'wifi_interface': 'Wi-Fi',
                'wifi_profiles': 'Tutti i profili utente',
                'owner': 'Proprietario registrato'
            },
            'es_ES': {
                'wifi_interface': 'Wi-Fi',
                'wifi_profiles': 'Todos los perfiles de usuario',
                'owner': 'Propietario registrado'
            },
            'fr_FR': {
                'wifi_interface': 'Wi-Fi',
                'wifi_profiles': 'Tous les profils utilisateurs',
                'owner': 'Propriétaire enregistré'
            },
            'de_DE': {
                'wifi_interface': 'Wi-Fi',
                'wifi_profiles': 'Alle Benutzerprofile',
                'owner': 'Registrierter Besitzer'
            },
            'pt_PT': {
                'wifi_interface': 'Wi-Fi',
                'wifi_profiles': 'Todos os perfis de usuário',
                'owner': 'Proprietário registrado'
            },
            'ru_RU': {
                'wifi_interface': 'Wi-Fi',
                'wifi_profiles': 'Все профили пользователей',
                'owner': 'Зарегистрированный владелец'
            },
            'zh_CN': {
                'wifi_interface': 'Wi-Fi',
                'wifi_profiles': '所有用户配置文件',
                'owner': '注册用户'
            },
            'ja_JP': {
                'wifi_interface': 'Wi-Fi',
                'wifi_profiles': 'すべてのユーザープロファイル',
                'owner': '登録所有者'
            },
            'ko_KR': {
                'wifi_interface': 'Wi-Fi',
                'wifi_profiles': '모든 사용자 프로필',
                'owner': '등록된 소유자'
            }
        }
        self.current_language = locale.getdefaultlocale()[0]

    def get_language_terms(self):
        return self.language_terms.get(self.current_language, self.language_terms['en_US'])
    
    def get_windows_mail(self):
        """Retrieve the email of the registered owner of the computer.

        This method searches the system information for the registered owner's email.
        It returns a message indicating whether an email address was found.

        Returns:
            str: A message indicating the email found or that none was found.

        Raises:
            subprocess.CalledProcessError: If the command fails to execute.
            UnicodeDecodeError: If there is an error decoding the command output.

        Note:
        This method is compatible only with Windows.
        """
        if platform.system() == "Windows":
            terms = self.get_language_terms()
            try:
                mail_output = subprocess.check_output("systeminfo", shell=True, text=True, encoding='latin-1')
                for line in mail_output.splitlines():
                    if terms['owner'] in line:
                        owner = line.split(":")[1].strip()
                        if '@' in owner:
                            return f"Mail Found: {owner}"
                        else:
                            return "No Emails Found."
            except subprocess.CalledProcessError as e:
                return f"Error: {e}"
            except UnicodeDecodeError as e:
                return f"Error: {e}"
            

            
            
