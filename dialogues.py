import time
def start_Dialogue():
    print("""Ты очнулся в одиночестве в чужом доме. Ужасно болит голова. """)
    input("Осмотреться... |Enter, чтобы продолжить.")
    print("""За столом в другом конце комнаты сидел мужчина. Увидев, что ты очнулся, он встал и направился к тебе.""")
    input()
    def print_slowly(text, delay = 0.1):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
    text_to_print = "Проснулся, самурай?"
    print_slowly((text_to_print))