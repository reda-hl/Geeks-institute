{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOXzB9OEoUxJEQooA3TV+Z6",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/reda-hl/Geeks-institute/blob/main/week2/Day2/ExerciceXP/calculator.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Create a file called operators.py.\n",
        "\n",
        "\n",
        "\n",
        "Create 2 functions:\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "addOperator(x, y) that returns the addition of 2 numbers.\n",
        "\n",
        "\n",
        "\n",
        "divideOperator(x, y) that returns the division of 2 numbers.\n",
        "\n",
        "\n",
        "\n",
        "Create another file called calculator.py, and import the operators module.\n",
        "\n",
        "\n",
        "\n",
        "Call the 2 functions and display the results.\n",
        "\n",
        "\n",
        "\n",
        "Do this process 3 times:\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "Once by importing the whole module.\n",
        "\n",
        "\n",
        "\n",
        "The second time by importing specific functions.\n",
        "\n",
        "\n",
        "\n",
        "The third time by using alias."
      ],
      "metadata": {
        "id": "23iPVfDlemZw"
      }
    },
    {
      "cell_type": "code",
      "execution_count": 8,
      "metadata": {
        "id": "NNcYEu2gZNGR",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "97c1982c-f8eb-4a23-89ca-f7b1a87106ac"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "by importing the whole module. // -- Add Fonction : 9   Dvide Fonction : 5.0   \n",
            "by importing specific functions. // -- Add Fonction : 20\n",
            "by using alias // -- Add Fonction : 9   Dvide Fonction : 5.714285714285714   \n"
          ]
        }
      ],
      "source": [
        "import operators\n",
        "from operators import addOperator\n",
        "from operators import addOperator as add , divideOperator as div\n",
        "\n",
        "print(f'by importing the whole module. // -- Add Fonction : {operators.addOperator(5,4)}   Dvide Fonction : {operators.divideOperator(20,4)}   '  )\n",
        "print(f'by importing specific functions. // -- Add Fonction : {addOperator(14,6)}'  )\n",
        "print(f'by using alias // -- Add Fonction : {add(5,4)}   Dvide Fonction : {div(40,7)}   '  )\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# !git clone https://github.com/reda-hl/Geeks-institute.git\n",
        "# cd /content/Geeks-institute/week2/Day2/ExerciceXP/"
      ],
      "metadata": {
        "id": "O-NLfFoTpAMN"
      },
      "execution_count": 9,
      "outputs": []
    }
  ]
}