import xml.etree.ElementTree as ET

# Carrega o XML
tree = ET.parse('xmltv.xml')
root = tree.getroot()

# Cria o arquivo M3U
with open('playlist.m3u', 'w', encoding='utf-8') as f:  # <-- CORRIGIDO (adição do ':')
    f.write('#EXTM3U\n')
    
    for channel in root.findall('.//channel'):
        channel_id = channel.get('id')
        name = channel.find('display-name').text if channel.find('display-name') is not None else channel_id
        url = channel.find('url').text if channel.find('url') is not None else None
        
        # Se não houver <url>, procura em <icon src> ou outros atributos
        if url is None:
            icon = channel.find('icon')
            if icon is not None and 'http' in icon.get('src', ''):
                url = icon.get('src')  # Usa o ícone como URL (se for um stream)
        
        if url:
            f.write(f'#EXTINF:-1 tvg-id="{channel_id}" tvg-name="{name}" group-title="Canais",{name}\n')
            f.write(f'{url}\n')

print("Playlist gerada: 'playlist.m3u'")
