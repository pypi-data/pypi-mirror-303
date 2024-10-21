import locale
import subprocess
import platform

class WifiPassword: 
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

    def get_wifi_pass(self):
        """Retrieve Wi-Fi profiles and their corresponding keys from the system.

        This method checks for available Wi-Fi interfaces and retrieves the saved Wi-Fi 
        profiles along with their security keys. It filters out disconnected interfaces 
        and only returns profiles associated with active Wi-Fi interfaces.

        Returns:
            str: A message containing the Wi-Fi interfaces and their associated profiles 
            with keys, or messages indicating if no interfaces or profiles were found.

        Raises:
            subprocess.CalledProcessError: If any command executed via subprocess fails.
        
        Note:
            This method is compatible only with Windows.

        Example:
            Example output:
            Interfaccia Wi-Fi: Wi-Fi
            Profile: HomeNetwork | Key: mySecretPassword
            Profile: WorkNetwork | Key: workPassword123
    """
        if platform.system() == "Windows":
            terms = self.get_language_terms()
            try:
                interfaces_output = subprocess.check_output("netsh interface show interface", shell=True, text=True)
                profiles_output = subprocess.check_output("netsh wlan show profiles", shell=True, text=True)

                interfaces = []
                for line in interfaces_output.splitlines():
                    if terms['wifi_interface'] in line and "Disconnesso" not in line:
                        interface_name = line.split()[-1]
                        interfaces.append(interface_name)

                profiles = []
                for line in profiles_output.splitlines():
                    if terms['wifi_profiles'] in line:
                        profile_name = line.split(":")[1].strip()
                        profiles.append(profile_name)

                if not interfaces:
                    return "No Wi-Fi interface found!"
                
                if not profiles:
                    return "No Wi-Fi profiles found!"

                results = []
                for interface in interfaces:
                    results.append(f"Interfaccia Wi-Fi: {interface}")
                    for profile in profiles:
                        profile_details = subprocess.check_output(f"netsh wlan show profile name=\"{profile}\" key=clear", shell=True, text=True)
                        for line in profile_details.splitlines():
                            if "Contenuto chiave" in line:
                                key_content = line.split(":")[1].strip()
                                results.append(f"Profile: {profile} | Key: {key_content}")

                return "\n".join(results)

            except subprocess.CalledProcessError as e:
                return f"Error: {e}"
