import requests
import random
import threading
import time

# Telegram bot details
TELEGRAM_BOT_TOKEN = '7210842351:AAGDw_JRRChT5uGFyHyii7LFgDeXDRE7WYI'
TELEGRAM_CHAT_ID = '6410755243'

# Discord account with authorization token
discord_account = {
    'auth_token': 'MTExODg1OTg0ODczODY2ODYXrnBu5IM12XigOwd2vXtdo9STVKd3I',
}

# Channel IDs to send messages to
channel_ids = [
    '1250830980466475109', #spanishhenryLEVEL16
    '1255240700493172908', #THAIBKT
    '1260569795431235658', #xebraeruopeLEVEL8OR16
    '1238764463218360341', #routexthai
    '995987691911008276', #kromnibtc
    '1271008054950891640', #koreamosaic
    '1267921158549012591', #PORTUGESINTRESTPROTOCOL
    '1268531002679099465', #nigeriamovefries
    '1242062200722423900', #ARABICAVINTUS
    # Add more channel IDs as needed
]

# Random messages to send
messages = [
    "Hello there!",
   "How do you express movement!",  
"What inspires your movement choices!",  
"What movements bring you joy!",  
"How do you explore movement!",  
"What motivates your movement journey!",  
"What's your ideal movement experience!",  
"How do you connect through movement!",  
"What challenges do you face!",  
"What's your favorite movement practice!",  
"How does movement inspire creativity!",  
"What movements resonate with you!",  
"How do you celebrate movement!",  
"What role does community play!",  
"How do you define movement!",  
"What's your vision for movement!",  
"How does movement impact you!",  
"What's your approach to movement!",  
"What's your favorite movement memory!",  
"How do you find joy!",  
"What movements shape your identity!",  
"What's your ideal movement space!",  
"How do you connect with others!",  
"What's your favorite movement style!",  
"How do you balance movement!",  
"What movements challenge your limits!",  
"How do you explore new techniques!",  
"What's your favorite way to move!",  
"How do you honor your body!",  
"What movements do you want to try!",  
"How do you stay motivated!",  
"What inspires your movement goals!",  
"How does movement enhance well-being!",  
"What's your favorite movement exercise!",  
"How do you incorporate play!",  
"What's your dream movement project!",  
"How do you share your movement!",  
"What does freedom in movement mean!",  
"How do you find rhythm!",  
"What's your favorite way to unwind!",  
"How do you foster creativity!",  
"What's your take on movement art!",  
"How do you explore personal expression!",  
"What role does nature play!",  
"How do you overcome challenges!",  
"What inspires your movement journey!",  
"How do you express emotions through movement!",  
"What's your ideal way to learn!",  
"What role does gratitude play!",  
"How do you celebrate achievements!",  
"What movements inspire your creativity!",  
"How do you adapt your practice!",  
"What's your approach to mindful movement!",  
"How do you cultivate curiosity!",  
"What movements connect you to culture!",  
"How do you engage with movement!",  
"What's your vision for the future!",  
"How do you encourage exploration!",  
"What's your favorite movement mantra!",  
"How do you stay open to new experiences!",  
"What's your favorite way to document movement!",  
"How do you find inspiration daily!",  
"What does vulnerability in movement mean!",  
"How do you share joy through movement!",  
"What's your perspective on movement community!",  
"How do you reflect on your journey!",  
"What's your ideal way to inspire others!",  
"How do you embrace change in movement!",  
"What role does imagination play!",  
"How do you integrate movement into daily life!",  
"What's your favorite way to combine art and movement!",  
"How do you connect with your inner child!",  
"What's your favorite way to play with movement!",  
"How do you honor your journey!",  
"What inspires you to keep moving!",  
"What's your take on movement as therapy!",  
"How do you cultivate resilience through movement!",  
"What's your ideal movement environment!",  
"How do you celebrate diversity in movement!",  
"What does self-discovery through movement look like!",  
"How do you encourage creativity in others!",  
"What's your favorite way to explore movement cultures!",  
"How do you find balance in life!",  
"What movements resonate with your emotions!",  
"How do you inspire freedom in movement!",  
"What's your approach to connecting with others!",  
"How do you express yourself through movement!",  
"What's your vision for community movement!",  
"How do you encourage others to move!",  
"What role does reflection play in growth!",  
"How do you cultivate joy through movement!",  
"What's your favorite way to explore new styles!",  
"How do you find peace in movement!",  
"What movements challenge your creativity!",  
"How do you foster a growth mindset!",  
"What's your take on movement education!",  
"How do you celebrate progress in movement!",  
"What inspires your personal movement journey!",  
"How do you adapt to different environments!",  
"What's your ideal way to document experiences!",  
"How do you incorporate movement into your creativity!",  
"What movements bring you peace!",  
"How do you explore your identity through movement!",  
"What's your approach to finding joy!",  
"How do you engage with your community!",  
"What movements connect you to your roots!",  
"How do you celebrate small victories!",  
"What's your favorite way to unwind!",  
"How do you stay curious about movement!",  
"What inspires your daily movement practice!",  
"How do you connect with your body!",  
"What's your vision for movement in society!",  
"How do you explore creativity through movement!",  
"What movements challenge your perceptions!",  
"How do you foster creativity in movement!",  
"What's your ideal vision for future movement!",  
"How do you celebrate the journey!",  
"What inspires your movement exploration!",  
"How do you encourage others to express themselves!",  
"What's your take on movement as connection!",  
"How do you integrate movement into your lifestyle!",  
"What's your favorite way to challenge yourself!",  
"How do you express joy through movement!",  
"What movements resonate with your identity!",  
"How do you stay connected to your passion!",  
"What's your ideal way to learn movement!",  
"How do you engage with your creative side!",  
"What inspires your movement stories!",  
"How do you celebrate diversity in your practice!",  
"What's your favorite way to share movement experiences!",  
"How do you stay motivated in your journey!",  
"What movements have a lasting impact on you!",  
"How do you connect with others through shared experiences!",  
"What's your vision for personal growth in movement!",  
"How do you encourage exploration in your practice!",   
    # (Add more messages here)
]

# Track failed deletion attempts per channel
failed_deletion_count = {channel_id: 0 for channel_id in channel_ids}

def send_message(auth_token, channel_id):
    headers = {
        'Authorization': auth_token
    }

    payload = {'content': random.choice(messages)}  # Choose a random message
    r = requests.post(f'https://discord.com/api/v9/channels/{channel_id}/messages', json=payload, headers=headers)

    if r.status_code == 200:
        message_id = r.json()['id']  # Get the message ID
        print(f'Message sent to channel {channel_id} with ID: {message_id}')

        # Delete the message immediately using threading
        threading.Thread(target=delete_message, args=(auth_token, channel_id, message_id)).start()
    else:
        print(f'Failed to send message to channel {channel_id}: {r.status_code} - {r.text}')
        notify_telegram(auth_token, r.status_code, 'send')

def delete_message(auth_token, channel_id, message_id):
    headers = {
        'Authorization': auth_token
    }
    delete_url = f'https://discord.com/api/v9/channels/{channel_id}/messages/{message_id}'
    delete_response = requests.delete(delete_url, headers=headers)

    if delete_response.status_code == 204:
        print(f'Message {message_id} deleted from channel {channel_id} successfully.')
    else:
        print(f'Failed to delete message {message_id} from channel {channel_id}: {delete_response.status_code} - {delete_response.text}')
        notify_telegram(auth_token, delete_response.status_code, 'delete')

        # Increment the failed deletion count for the channel
        failed_deletion_count[channel_id] += 1

        # Stop sending messages to this channel if the failed deletion count exceeds 3
        if failed_deletion_count[channel_id] > 3:
            print(f"Exceeded deletion failure limit for channel {channel_id}. Stopping further messages to this channel.")
            # Remove the channel from the list
            channel_ids.remove(channel_id)

def notify_telegram(auth_token, error_code, action):
    message = f"Account Token: {auth_token}\nAction: {'Send' if action == 'send' else 'Delete'} failed\nError Code: {error_code}"
    payload = {'chat_id': TELEGRAM_CHAT_ID, 'text': message}
    requests.post(f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage', json=payload)

def process_channel(auth_token, channel_id):
    send_message(auth_token, channel_id)

def main():
    for _ in range(2000):  # Repeat the process 2000 times
        threads = []
        for channel_id in list(channel_ids):  # Use a copy of channel_ids to avoid modification during iteration
            # Send and delete messages in all channels simultaneously
            t = threading.Thread(target=process_channel, args=(discord_account['auth_token'], channel_id))
            t.start()
            threads.append(t)
        
        # Wait for all threads to complete
        for t in threads:
            t.join()

        print("Completed an iteration. Waiting for 5 minutes before the next iteration.")
        time.sleep(120)  # Wait for 2 minutes (120 seconds) before the next iteration

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        notify_telegram('N/A', str(e), 'bot stopped')
