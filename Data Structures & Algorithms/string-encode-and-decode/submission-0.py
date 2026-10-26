class Solution:

    def encode(self, strs: List[str]) -> str:
        """
        Transforma uma lista de strings em uma unica string.

        Exemplo:
            ["ola", "mundo"] -> "3,5,#olamundo"
        """

        # Se a lista estiver vazia, retorna uma string vazia.
        # Atencao: [] e diferente de [""], que contem uma string vazia.
        if not strs:
            return ""

        # sizes: guarda o tamanho de cada string.
        # res: guarda as partes que formarao a string codificada.
        sizes, res = [], []

        # Percorre as strings e registra seus tamanhos.
        # Exemplo: ["ola", "mundo"] -> sizes = [3, 5]
        for s in strs:
            sizes.append(len(s))

        # Monta o cabecalho com os tamanhos separados por virgulas.
        for sz in sizes:
            # Converte o tamanho inteiro para texto.
            res.append(str(sz))

            # Cada tamanho termina com uma virgula.
            res.append(',')

        # Marca o fim do cabecalho e o inicio do conteudo.
        # Neste ponto: res = ["3", ",", "5", ",", "#"]
        res.append('#')

        # Adiciona cada string original como um elemento de res.
        # extend adiciona os elementos da lista, nao a lista inteira.
        # Agora: res = ["3", ",", "5", ",", "#", "ola", "mundo"]
        res.extend(strs)

        # Junta todas as partes, sem separador entre elas.
        # Resultado: "3,5,#olamundo"
        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        """
        Recupera a lista original a partir da string codificada.

        Espera uma entrada valida, produzida pelo metodo encode.

        Exemplo:
            "3,5,#olamundo" -> ["ola", "mundo"]
        """

        # Uma string codificada vazia representa uma lista vazia.
        if not s:
            return []

        # sizes: tamanhos recuperados do cabecalho.
        # res: strings reconstruidas.
        # i: indice da posicao atual na string codificada.
        sizes, res, i = [], [], 0

        # Le o cabecalho ate encontrar o marcador "#".
        while s[i] != '#':

            # i marca o inicio do numero.
            # j avanca para encontrar a virgula que encerra esse numero.
            j = i

            while s[j] != ',':
                j += 1

            # O fatiamento s[i:j] inclui i, mas nao inclui j.
            # Portanto, captura o numero sem a virgula.
            # int converte esse texto em um tamanho inteiro.
            sizes.append(int(s[i:j]))

            # Pula a virgula e posiciona i no proximo numero
            # ou no marcador "#", caso o cabecalho tenha terminado.
            i = j + 1

        # Ao sair do while, i aponta para "#".
        # Avanca uma posicao para chegar ao inicio do conteudo.
        i += 1

        # Recupera uma string para cada tamanho registrado.
        for sz in sizes:

            # Extrai exatamente sz caracteres a partir de i.
            # Exemplo: se sz = 3, recupera os proximos 3 caracteres.
            res.append(s[i:i + sz])

            # Avanca para o inicio da proxima string.
            i += sz

        # Retorna a lista reconstruida.
        return res