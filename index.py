from telethon import TelegramClient, events, utils
from json import loads
from modules import Validation

if __name__ == '__main__':
    with open('config.json', 'r') as file:
        ressult = file.read()

    global result
    result = loads(ressult)
    global client
    client = TelegramClient('The Storage', result['tg-api-id'], result['tg-api-hash'])
    global spam
    spam = ['t.me/', 'instagram.com/', 'facebook.com/', 'tiktok.com/', 'youtube.com/c/', 'youtube.com/channel/', 'youtube.com/watch', 'twitter.com/', 'youtu.be/', 'sell', 'buy'] #Add The All Keywords You Need
    cache_card = None

    @client.on(events.NewMessage())
    async def handler(event):
        global cache_card
        if(str(utils.get_peer_id(event.peer_id)) in result['dont-scrape-from']):
            return

        if(event.file != None and event.file.name != None):
            t = -1
            while True:
                try:
                    t = event.file.name.index(".", t + 1)
                    point = t
                except ValueError:
                    break
            extension = event.file.name[point : len(event.file.name)]
            check = Validation.ValidateFiles(extension, result['targets'])
            if(check.result != False):
                if(result['save']['enabled']):
                    await client.send_message(result['save']['place'], '#' + check.result)
                    await client.send_message(result['save']['place'], event.message)
                if(result['download']):
                    await client.download_media(message=event.message, file='Downloads/' + check.result + '/' + event.file.name)
                

        if(event.message.buttons != None):
            for a in event.message.buttons:
                if(a[0].url != None):
                    check = Validation.ValidateText(a[0].url, result['targets'])
                    if(check.result != False):
                        if(result['save']['enabled']):
                            await client.send_message(result['save']['place'], '#' + check.result)
                            await client.send_message(result['save']['place'], event.message)
                            await client.send_message(result['save']['place'], a[0].url)
                        if(result['download']):
                            with open('Downloads/' + check.result + '.txt', 'a', encoding='utf-8') as file:
                                file.write(a[0].url + '\n')
                        


        if(event.message.video != None and result['targets']['videos']):
            if(result['save']['enabled']):
                await client.send_message(result['save']['place'], '#Video')
                await client.send_message(result['save']['place'], event.message)
            if(result['download']):
                    await client.download_media(message=event.message, file='Downloads/Videos/' + event.file.name)
            

        if(event.message.photo != None and result['targets']['images']):
            if(result['save']['enabled']):
                await client.send_message(result['save']['place'], '#Image')
                await client.send_message(result['save']['place'], event.message)
            if(result['download']):
                    await client.download_media(message=event.message, file='Downloads/Images/')
            

        if(bool(event.message.audio != None or event.message.voice != None) and result['targets']['audios']):
            if(result['save']['enabled']):
                await client.send_message(result['save']['place'], '#Audio')
                await client.send_message(result['save']['place'], event.message)
            if(result['download']):
                    await client.download_media(message=event.message, file='Downloads/Audios/')
            
        
        if(result['targets']['spam']):
            for i in spam:
                if(event.raw_text.find(i) != -1):
                    if(result['save']['enabled']):
                        await client.send_message(result['save']['place'], '#Spam')
                        await client.send_message(result['save']['place'], event.message)
                    if(result['download']):
                        with open('Downloads/' + 'Spam.txt', 'a', encoding='utf-8') as file:
                            file.write(event.raw_text + '\n')
                        

        check = Validation.ValidateText(event.raw_text, result['targets'])
        if(check.result != False):
            if(check.result == 'Card'):
                if(check.card == cache_card):
                    return
                else:
                    cache_card = check.card
            if(result['save']['enabled']):
                await client.send_message(result['save']['place'], '#' + check.result)
                await client.send_message(result['save']['place'], event.message)
            if(result['download']):
                with open('Downloads/' + check.result + '.txt', 'a', encoding='utf-8') as file:
                    file.write(event.raw_text + '\n')

                

    client.start()
    client.run_until_disconnected()