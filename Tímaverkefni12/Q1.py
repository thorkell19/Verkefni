#definition for music_func goes here
def music_func(music_type = "Classic Rock", music_group = "The Beatles", vocalist = "Freddie Mercury"):
    print("The best type of music is", music_type)
    print("The best music group is", music_group)
    print("The best lead vocalist is", vocalist)
    return music_type, music_group, vocalist

def main():
    music, group, singer = input("Input music, group, singer: ").split(',')
    music_func(music, group, singer)
    music_func()

main()