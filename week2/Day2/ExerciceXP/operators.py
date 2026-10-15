{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOpbWc1CLr2NhPz4bSbP+c1",
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
        "<a href=\"https://colab.research.google.com/github/reda-hl/Geeks-institute/blob/main/week2/Day2/ExerciceXP/operators.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
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
      "execution_count": 29,
      "metadata": {
        "id": "NNcYEu2gZNGR"
      },
      "outputs": [],
      "source": [
        "def addOperator(x, y):\n",
        "  return x+y\n",
        "\n",
        "def divideOperator(x, y):\n",
        "  return"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!git clone https://github.com/reda-hl/Geeks-institute.git"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "m9iFgG_bgnUg",
        "outputId": "c74354a0-d917-4043-ff08-e2316fdf6e20"
      },
      "execution_count": 22,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Cloning into 'Geeks-institute'...\n",
            "remote: Enumerating objects: 217, done.\u001b[K\n",
            "remote: Counting objects: 100% (217/217), done.\u001b[K\n",
            "remote: Compressing objects: 100% (201/201), done.\u001b[K\n",
            "remote: Total 217 (delta 113), reused 13 (delta 0), pack-reused 0 (from 0)\u001b[K\n",
            "Receiving objects: 100% (217/217), 43.91 KiB | 936.00 KiB/s, done.\n",
            "Resolving deltas: 100% (113/113), done.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "cd Geeks-institute/week2/Day2/ExerciceXP/"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "PgAejQj7g8Nz",
        "outputId": "31246b36-ca4c-493f-8b49-c94ce8dfaf8e"
      },
      "execution_count": 25,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "/content/Geeks-institute/week2/Day2/ExerciceXP/Geeks-institute/week2/Day2/ExerciceXP\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!ls"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "4DlNStnxg540",
        "outputId": "159cd734-3aed-4de3-a59b-ddf81b4b4bc1"
      },
      "execution_count": 26,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            " Exercise_1_Dunder_Methods.ipynb   operators.ipynb\n",
            "' Exercise 2 : Exceptions.ipynb'   README.md\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [],
      "metadata": {
        "id": "eAyF4_PChtDN"
      }
    }
  ]
}