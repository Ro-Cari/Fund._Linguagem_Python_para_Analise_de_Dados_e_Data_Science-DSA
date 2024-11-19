{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Ro-Cari/Fund._Linguagem_Python_para_Analise_de_Dados_e_Data_Science-DSA/blob/main/Cap04_exercicios_resolvido.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Er3ysB0cWy9w"
      },
      "source": [
        "# <font color='blue'>Data Science Academy</font>\n",
        "\n",
        "## <font color='blue'>Fundamentos de Linguagem Python Para Análise de Dados e Data Science</font>\n",
        "\n",
        "## <font color='blue'>Capítulo 4 - Exercícios</font>"
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "JKPt6HjI1WpV"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "rtYogo_2Wy91",
        "outputId": "cb3ce239-747e-455b-e512-8289d7aa24d2"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Versão da Linguagem Python Usada Neste Jupyter Notebook: 3.10.12\n"
          ]
        }
      ],
      "source": [
        "# Versão da Linguagem Python\n",
        "from platform import python_version\n",
        "print('Versão da Linguagem Python Usada Neste Jupyter Notebook:', python_version())"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "0MQzF7VEWy93"
      },
      "source": [
        "## Exercícios"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "X83WNAPVWy93"
      },
      "outputs": [],
      "source": [
        "# Exercício 1 - Imprima na tela os números de 1 a 10. Use uma lista para armazenar os números."
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\n",
        "lista"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "9Huov2nW9LAC",
        "outputId": "24b129b2-6582-4b6b-e283-58358b3cdc4a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]"
            ]
          },
          "metadata": {},
          "execution_count": 1
        }
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "8KeQ_R02Wy94",
        "outputId": "15c9adb2-4b7a-431d-f588-8190f2f1cdac"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "['obj1', 'obj2', 'obj3', 'obj4', 'obj5']"
            ]
          },
          "metadata": {},
          "execution_count": 2
        }
      ],
      "source": [
        "# Exercício 2 - Crie uma lista de 5 objetos e imprima na tela\n",
        "lista2 = [\"obj1\", \"obj2\", \"obj3\", \"obj4\", \"obj5\"]\n",
        "lista2"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "krk400m4Wy94"
      },
      "outputs": [],
      "source": [
        "# Exercício 3 - Crie duas strings e concatene as duas em uma terceira string"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "texto1 = \"Olá, \"\n",
        "texto2 = \"mundo!\"\n",
        "texto3 = texto1 + texto2\n",
        "texto3"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 36
        },
        "id": "esVWzG469o6y",
        "outputId": "910441b1-8545-454e-e51d-a9cb8c521fc0"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'Olá, mundo!'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 4
        }
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "qskbz49EWy94",
        "outputId": "fe7d894f-cd4d-4887-fe5c-4f4e285c6790"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "3"
            ]
          },
          "metadata": {},
          "execution_count": 5
        }
      ],
      "source": [
        "# Exercício 4 - Crie uma tupla com os seguintes elementos: 1, 2, 2, 3, 4, 4, 4, 5 e depois utilize a função count do\n",
        "# objeto tupla para verificar quantas vezes o número 4 aparece na tupla\n",
        "tupla =(1, 2, 2, 3, 4, 4, 4, 5)\n",
        "tupla.count(4)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "GgnGJzWEWy95",
        "outputId": "a3c3c2e4-2bbf-42e8-c74e-7b46144d51ff"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "{}"
            ]
          },
          "metadata": {},
          "execution_count": 6
        }
      ],
      "source": [
        "# Exercício 5 - Crie um dicionário vazio e imprima na tela\n",
        "dic = {}\n",
        "dic"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "CCjlP2QbWy95"
      },
      "outputs": [],
      "source": [
        "# Exercício 6 - Crie um dicionário com 3 chaves e 3 valores e imprima na tela"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "dic2 = {\"Roberta\": 25, \"Leonardo\": 16}\n",
        "dic2"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "nAPtFBTK-O9C",
        "outputId": "d66861da-cedf-42fd-9914-b23a02500334"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "{'Roberta': 25, 'Leonardo': 16}"
            ]
          },
          "metadata": {},
          "execution_count": 7
        }
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "B1b1gzqPWy96"
      },
      "outputs": [],
      "source": [
        "# Exercício 7 - Adicione mais um elemento ao dicionário criado no exercício anterior e imprima na tela"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "dic2[\"Maria\"]=63\n",
        "dic2"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "m6L9t27--wrh",
        "outputId": "c05d1747-3487-42a4-fe22-4ba237c7c5a6"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "{'Roberta': 25, 'Leonardo': 16, 'Maria': 63}"
            ]
          },
          "metadata": {},
          "execution_count": 11
        }
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "ZjM9oAOoWy96"
      },
      "outputs": [],
      "source": [
        "# Exercício 8 - Crie um dicionário com 3 chaves e 3 valores.\n",
        "# Um dos valores deve ser uma lista de 2 elementos numéricos.\n",
        "# Imprima o dicionário na tela."
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "dic3 = {\"Chave\":1, \"Chave2\":[2, 30], \"Chave3\":4 }\n",
        "dic3"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "_kMrn3bU_tMD",
        "outputId": "47293fa5-18b5-4ad3-c571-8cc4574dae35"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "{'Chave': 1, 'Chave2': [2, 30], 'Chave3': 4}"
            ]
          },
          "metadata": {},
          "execution_count": 15
        }
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "n0mfqWgxWy96"
      },
      "outputs": [],
      "source": [
        "# Exercício 9 - Crie uma lista de 4 elementos. O primeiro elemento deve ser uma string,\n",
        "# o segundo uma tupla de 2 elementos, o terceiro um dcionário com 2 chaves e 2 valores e\n",
        "# o quarto elemento um valor do tipo float.\n",
        "# Imprima a lista.\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "Lista3 = [\"Texto1\",(1, 2), {\"Chave1\":1, \"Chave2\":2}, 10.0]\n",
        "Lista3\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "QcWzX30KAvts",
        "outputId": "d331a577-a275-4e13-eae3-fbe612ca50df"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "list"
            ]
          },
          "metadata": {},
          "execution_count": 18
        }
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "zhsfaIz4Wy96"
      },
      "outputs": [],
      "source": [
        "# Exercício 10 - Considere a string abaixo. Imprima na tela apenas os caracteres da posição 1 a 18.\n",
        "frase = 'Cientista de Dados é o profissional mais sexy do século XXI'"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "frase = 'Cientista de Dados é o profissional mais sexy do século XXI'\n",
        "frase[0:18]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 36
        },
        "id": "fV6RBLv5BvML",
        "outputId": "00d11a1c-292a-4b15-a82b-8e09daf6b51c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'Cientista de Dados'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 20
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "USekXdDBWy97"
      },
      "source": [
        "# Fim"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "MhqngVlnWy97"
      },
      "source": [
        "### Obrigado\n",
        "\n",
        "### Visite o Blog da Data Science Academy - <a href=\"http://blog.dsacademy.com.br\">Blog DSA</a>"
      ]
    }
  ],
  "metadata": {
    "kernelspec": {
      "display_name": "Python 3 (ipykernel)",
      "language": "python",
      "name": "python3"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "ipython",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.9.13"
    },
    "colab": {
      "provenance": [],
      "name": "Cap04-exercicios_resolvido.py",
      "include_colab_link": true
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}