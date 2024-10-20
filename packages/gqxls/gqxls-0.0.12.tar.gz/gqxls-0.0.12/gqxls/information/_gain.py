import random, secrets
class gain:
    def get_random_file_name(self,length_character: int)->str:
        if length_character <= 0:
            raise ValueError(f"length_character:{length_character}必须大于0")
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        if length_character > len(alphabet):
            return ''.join(secrets.choice(alphabet) for _ in range(length_character))
        else:
            return ''.join(random.sample(alphabet, length_character))