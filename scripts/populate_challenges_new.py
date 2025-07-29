import os
import sys
import django

# Add the project directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'santheCTF.settings')
django.setup()

from ctf.models import Challenge

def populate_challenges():
    # Clear existing challenges
    Challenge.objects.all().delete()
    
    challenges = [
            {
                'title': 'Sanity Check (100)',
                'description': 'Welcome to RVU Santhe Mini-CTF! Look through our WhatsApp group (https://chat.whatsapp.com/L9fkgEKsQd1IR0PjV5Xbvd) to get the flag! Flag format: mctf{text}',
                'points': 100,
                'flag': 'mctf{W3lc0m3_t0_RVU_Santhe_Mini_CTF}'
            },
            {
                'title': 'Vinegar (300) - skibidi',
                'description': 'Can you decode this message? Note: Wrap the decrypted text in mctf{} n1q3v3s3_k1sp3j key: skibidi',
                'points': 300,
                'flag': 'mctf{v1g3n3r3_c1ph3r}'
            },
            {
                'title': 'Vinegar (300) - ohio',
                'description': 'Can you decode this message? Note: Wrap the decrypted text in mctf{} jposblz_qwwpsf key: ohio',
                'points': 300,
                'flag': 'mctf{vigener_cipher}'
            },
            {
                'title': 'Vinegar (300) - gyat',
                'description': 'Can you decode this message? Note: Wrap the decrypted text in mctf{} bgg3g3x3_aiincr key: gyat',
                'points': 300,
                'flag': 'mctf{vig3n3r3_cipher}'
            },
            {
                'title': 'Vinegar (300) - sigma',
                'description': 'Can you decode this message? Note: Wrap the decrypted text in mctf{} nqmqnwz3_i1bh3j key: sigma',
                'points': 300,
                'flag': 'mctf{vigener3_c1ph3r}'
            },
            {
                'title': 'Vinegar (300) - alpha',
                'description': 'Can you decode this message? Note: Wrap the decrypted text in mctf{} vtvlnec3_rpphpg key: alpha',
                'points': 300,
                'flag': 'mctf{vigener3_cipher}'
            },
            {
                'title': 'Vinegar (300) - beta',
                'description': 'Can you decode this message? Note: Wrap the decrypted text in mctf{} w1kxnfv3_v1pi3v key: beta',
                'points': 300,
                'flag': 'mctf{v1gener3_c1ph3r}'
            },
            {
                'title': 'Vinegar (300) - rizz',
                'description': 'Can you decode this message? Note: Wrap the decrypted text in mctf{} m1odmvz3_bhgpdq key: rizz',
                'points': 300,
                'flag': 'mctf{v1gener3_cipher}'
            },
            {
                'title': 'Vinegar (300) - fanum',
                'description': 'Can you decode this message? Note: Wrap the decrypted text in mctf{} a1grhqw3_cvjtjr key: fanum',
                'points': 300,
                'flag': 'mctf{v1gener3_cipher}'
            },
            {
                'title': 'Vinegar (300) - mogg',
                'description': 'Can you decode this message? Note: Wrap the decrypted text in mctf{} h1u3tkd3_q1vn3d key: mogg',
                'points': 300,
                'flag': 'mctf{v1g3ner3_c1ph3r}'
            },
            {
                'title': 'Where Blooming Flowers and Literature Meet (200)',
                'description': 'Livvy Dunn and Baby Gronkwant to buy books at the OG Bookstore. It\'s on a very popular street where interviews happen for no reason. Discover the name of the building opposite. Flag format: mctf{name}',
                'points': 200,
                'flag': 'mctf{am0eba}'
            },
            {
                'title': 'Stalking Skills (OSINT) (200)',
                'description': 'You\'re tracking down a missing flag left by a mysterious profile. They\'ve left pieces of it across CyberSec\'s social profiles. Follow the trail from Discord (https://discord.gg/UBykWwXsZP) to assemble the full flag.',
                'points': 200,
                'flag': 'mctf{3xc3ll3nt_5t4lk1ng_5k1ll5}'
            }
    ]

    for challenge in challenges:
        Challenge.objects.create(**challenge)

if __name__ == "__main__":
    populate_challenges()
    print("Challenges populated successfully.")
