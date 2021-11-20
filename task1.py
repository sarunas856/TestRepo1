skaitmens_simbolis = {'0':'zero', '1':'one', '2':'two', '3':'three', '4':'four', '5':'five', '6':'six', '7':'seven', '8':'eight', '9':'nine'}

def raidine_israiska(skaicius):
    target_list = []
    for number in skaicius:
        target_list += skaitmens_simbolis[number]
    return target_list
if __name__ == '__main__':
    while True:
        my_sequence = input('Give the sequence of numbers: ')
        result = raidine_israiska(my_sequence)
        print(f'{result})
        shall_continue = input('Do you want to continue ([y]/n]?: ')
        if shall_continue.lower () != 'y':
            break


