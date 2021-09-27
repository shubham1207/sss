from random import randint
def pick_random__word():
    word_list=["True", "Fail", "MAths", "physics", "Gaana", "SPotify", "numeric", "speaker", "Music", "Robot", "RObot 2", "Home", "House", "Housefull", "Housefull2","Housefull3", "Book", "Mouse", "Keybord", "Danger"]
    selected_index=randint(0, len(word_list)-1)
    return word_list[selected_index]


print(pick_random__word()) 

