class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Guarda a última posição em que cada caractere apareceu.
        last_seen = {}

        # Início da substring atual.
        left = 0

        # Maior tamanho encontrado.
        max_length = 0

        for right, char in enumerate(s):
            # Se o caractere já estiver dentro da janela atual,
            # movemos o início para depois da última ocorrência.
            if char in last_seen and last_seen[char] >= left:
                left = last_seen[char] + 1

            # Atualizamos a última posição do caractere.
            last_seen[char] = right

            # Tamanho da janela atual, incluindo as duas extremidades.
            current_length = right - left + 1
            max_length = max(max_length, current_length)

        return max_length