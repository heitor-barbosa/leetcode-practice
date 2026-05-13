# Merge Strings Alternately

> Resolução e anotações sobre o problema.

### Informações

| Campo | Valor |
|---|---|
| Link | [LeetCode - Merge Strings Alternately](https://leetcode.com/problems/merge-strings-alternately/description/) |
| Dificuldade | Easy |
| Categorias | Strings |

---

### Enunciado resumido
Dado duas strings x e y, juntar ambas em uma só, intercalando seus respectivos caracteres.

---

### Raciocínio e abordagem

Pensamento inicial: descobrir a maior palavra, iterar sobre seu tamanho, ir adicionando as letras sempre que possível.

Segunda análise: uso indevido de try catch, basta verificar se a posição atual excede o tamanho da palavra em questão;
armazenar chars em uma lista ao inves de string, para evitar criação constante de novas strings.

Outra Resolução (mostrada pelo leetcode):
Usar two pointers, não precisa descobrir a palavra maior, basta iterar sobre as duas com dois 'ponteiros'

---

### Complexidade

| Tipo | Complexidade |
|---|---|
| Tempo | O(n+m) |
| Espaço | O(1) |

---

### Aprendizados

- Abordagem two pointers