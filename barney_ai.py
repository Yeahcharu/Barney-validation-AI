# -*- coding: utf-8 -*-
"""barney_ai.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xuWp12oWjFcZi5DrUPGJ7bJYGmmrHWtB
"""
from openai import OpenAI

client = OpenAI(api_key="your key here")
from openai import OpenAI

client = OpenAI(api_key="your key here")
import time
import random
from plyer import notification


# Barney Stinson-style prompts
barney_prompts = [
    "Give me a legendary pep talk, Stinson style. Challenge accepted!",
    "Your programming finesse is legendary, just like my... wait for it... legendary playbooks!",
    "Give me a legendary pep talk, Stinson style. Challenge accepted, just like Ted on a quest for true love!",
    "Flaunt my coding skills with Barney-level swagger. Legen... wait for it... dary! It's like Marshall's love for charts, but with code!",
    "Motivate me with the charm of a suit-wearing coder. How would Barney do it? Picture this – you, coding like Lily paints, with grace and style!",
    "Inspire me with a coding mantra, Barney-style. Suit up and code on! It's like Robin chasing her dream job – relentless and legendary!",
    "Barney, I need a boost for my coding marathon. Lay some coding wisdom on me! Imagine coding with the precision of Ted's architecture dreams!",
    "Barney, charm me with a coding compliment that's as smooth as a pick-up line. How would you woo a coder? Your code, like Robin, is legendary and unforgettable!",
    "Barney, I need a coding boost that makes me feel as irresistible as your charm. Lay it on me, maestro! Channel your inner Robin – be bold, be legendary, and code with confidence!",
    "Flaunt my coding prowess with Barney's level of seductive swagger. Make the code sizzle, Stinson style! It's like Lily's artistic touch, but in the coding realm!",
    "Barney, treat my coding skills like a forbidden pleasure. Seduce me with a compliment only you can deliver. Your code, like Marshall's charts, is a visual masterpiece!",
    "Give me a coding pep talk, Stinson-style, that's so tempting it's almost illegal. How would you make my code legendary and sensual? Imagine coding like Ted pursues the perfect romantic gesture – with passion and flair!",
    "Imagine your code is a playbook for legendary tech conquests. Suit up, coder, and let's make this coding session legen... wait for it... dary!",
    "Your coding finesse is as precise as Robin's aim when she's on the news. Channel that legendary accuracy and make your code the headline!",
    "Suit up, because coding without style is like Marshall without Lily – incomplete. Let your code be the perfect love story, legendary and timeless.",
    "Your coding prowess is like a well-executed Bro Code play. Remember, a Bro is entitled to coding greatness, especially when the rest of his Bros are watching!",
    "Picture this: You, coding like Ted designing the perfect building. Precision, dedication, and the pursuit of legendary craftsmanship in every line of code.",
    "Your code is so impressive; it's the tech equivalent of a Barney Stinson pick-up line. Smooth, irresistible, and leaving a lasting impression on every compiler in the room!",
    "Coding like a Bro means embracing challenges with the confidence of Barney at MacLaren's. Legendary coders suit up, face challenges, and conquer the coding world!",
    "Your coding journey is like a legendary night at MacLaren's. It starts with a challenge, filled with legendary moments, and ends with a 'Haaaave you met Ted?' level of success.",
    "Is your code made of copper and tellurium? Because you've got that Cu-Te factor! Your code, like a charming element, leaves a lasting impression on every user.",
    "Your code is so legendary; it's like the 'Haaaaave you met Ted?' of the programming world. Suit up and make every line of code an introduction to coding greatness!",
    "Your coding skills are like Playbook Move #23 – 'The Legendary Line of Code.' It's smooth, irresistible, and leaves an indelible mark on every user's heart. Suit up, coder!",
    "Flaunt your coding prowess with the finesse of Playbook Move #17 – 'The Code Whisperer.' Whisper sweet nothings to your code, and watch it respond with legendary perfection.",
    "Suit up, because your code is executing Playbook Move #9 – 'The Tech Seduction.' Each line of code is a flirtatious invitation, enticing users into the world of legendary software.",
    "Imagine your code as Playbook Move #3 – 'The Irresistible Algorithm.' Just like a perfect algorithm, your code is designed to captivate, engage, and leave users wanting more.",
    "Your coding journey is a legendary playbook of its own, incorporating lessons from 'The Playbook' to create a legendary user experience. Suit up, embrace the lessons, and code with seductive precision.",
    "Picture this: You, coding with the confidence of Playbook Move #11 – 'The Tech Tease.' Tease your code into perfection, leaving users yearning for the next update.",
    "Channel the finesse of Playbook Move #8 – 'The Art of Code Seduction.' Your code is a masterpiece, each line a brushstroke of flirtatious genius. Suit up and let the seduction unfold!",
    "Your code is executing Playbook Move #5 – 'The Magnetic Algorithm.' It attracts users with a magnetic force, keeping them hooked and enchanted. Legendary coders know the power of attraction!",
    "Embrace Playbook Move #14 – 'The Suave Syntax.' Your code's syntax is so suave, it's like delivering pick-up lines to compilers. Suit up and let your syntax do the talking!",
    "In the legendary world of coding, Playbook Move #20  'The Code Charmer' reigns supreme. Your code is the charmer, leaving users bewitched, bothered, and bewildered. Suit up and let the charm unfold!",
    "Hey coding maestro, your skills are smoother than a perfectly executed pick-up line. If I were a compiler, I'd be blushing right now. Suit up, because your code is legendary and irresistible!",
    "Your coding finesse is so impressive; it's like you've stolen a page from my playbook. You're not just a coder; you're a legend in the making. Suit up, and let's conquer the coding world together!",
    "Flaunt that legendary coding prowess, because, wow, your code is making even me envious. It's like you've mastered the legendary art of charm and translated it into your programming. Impressive, my friend!",
    "If coding were a dance, you'd be leading with legendary precision. Your code is a seductive tango, leaving everyone in awe. Suit up, because your coding skills are turning heads – legendary style!",
    "Your code is so impressive; it's like a flawless execution of 'The Playbook.' You're not just coding; you're orchestrating a symphony of legendary programming. Suit up, maestro, and let the coding serenade continue!",
    "Is your code made of copper and tellurium? Because, damn, it's got that Cu-Te factor. Your coding skills are turning heads in a way only a legend like you could. Suit up, coding charmer!",
    "Your code is leaving me speechless, and that's saying something. It's like you've mastered the legendary art of charm, but with a keyboard. Suit up, because your coding prowess is truly legendary!",
    "If coding were a sport, you'd be the MVP. Your skills are scoring legendary points, and I'm here for the show. Suit up, coding superstar, because you're stealing the spotlight with your legendary code!",
    "Your coding journey is like a legendary love story, and I'm captivated by every line of code. It's as if you've written a playbook for irresistible programming. Suit up, and let the coding romance continue!",
    "I've seen some impressive code in my time, but yours is on another level. It's like you've cracked the code to legendary programming. Suit up, coding genius, because you've left me utterly impressed!",
    "Give me a coding pep talk, Stinson-style, that's so tempting it's almost illegal. How would you make my code legendary and sensual?",
    "Thus, if she’s this crazy, she has to be this hot.",
    "It's not legendary unless your friends are there to see it.",
    "Flaunt my coding skills with Barney-level swagger. Legen... wait for it... dary!",
    "Barney, treat my coding skills like a forbidden pleasure. Seduce me with a compliment only you can deliver.",
    "A Bro is always entitled to do something stupid, as long as the rest of his Bros are all doing it.",
    "Bro Code Article 1: Bros before code.",
    "Inspire me with a coding mantra, Barney-style. Suit up and code on!",
    "When I'm sad, I stop being sad and be awesome instead.",
    "Barney, I need a boost for my coding marathon. Lay some coding wisdom on me!",
    "Barney, charm me with a coding compliment that's as smooth as a pick-up line. How would you woo a coder?",
    "Barney, I need a coding boost that makes me feel as irresistible as your charm. Lay it on me, maestro!",
    "Never underestimate the power of the suit.",
]

def gen(prompt):
    
    response = client.completions.create(model="text-davinci-003",  # Specify the model name
    prompt=prompt,
    temperature=0.7,
    max_tokens=1000,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0)
    return response.choices[0].text


def notify(message, title):
    notification.notify(
        title=f'{Barneybros} 👔',  # Emoji of a tie
        message=message,
        app_icon=None,
        timeout=30,
    )

while True:
    if time.strftime('%M') in ['00', '05', '10', '15', '20', '25', '30', '35', '40', '45', '50', '55']:
        prompt = random.choice(barney_prompts)
        message = gen(prompt)
        notify(message, 'Barney Stinson')
        print('Did my job, going to sleep now.You know beauty sleep is kind of required for a person like me so hot , so i can be legend...i hope youre not lactose inteloerant because the next word is DARY.. Suit up and code on! 🚀', time.strftime("%H:%M:%S"))
        time.sleep(300)
        print('I am awake now, back to work chicas. Challenge accepted! 💼', time.strftime("%H:%M:%S"))
    else:
        continue
