{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "f4335eee",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a=4\n",
    "b=4\n",
    "x=5\n",
    "a==b"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "83a6c928",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a==b or b==a"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "6b7635b7",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "argument of type 'int' is not iterable",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[3], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m \u001b[43mx\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;129;43;01min\u001b[39;49;00m\u001b[43m \u001b[49m\u001b[43mb\u001b[49m\n",
      "\u001b[1;31mTypeError\u001b[0m: argument of type 'int' is not iterable"
     ]
    }
   ],
   "source": [
    "x in b"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "6078fb47",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "not a==b\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "58dde99f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\"desh\" in \"bangladesh\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "fccaf9a1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\"desh\" in \"bangadash\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "540f0a0a",
   "metadata": {},
   "outputs": [],
   "source": [
    "uni=['Brac', 'ewu', 'nsu']\n",
    "num=[1,2,3]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "993230be",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'ewu'"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "uni[1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "1a422271",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Brac', 'ewu', 'nsu']"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "uni[:3]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "fd63d641",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Brac', 'ewu', 'nsu']"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "uni[0:]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "e594649e",
   "metadata": {},
   "outputs": [],
   "source": [
    "uni.append('buet')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "ea3fb46e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Brac', 'ewu', 'nsu', 'buet']"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "uni"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "8f9d33d8",
   "metadata": {},
   "outputs": [],
   "source": [
    "uni.insert(1,'kuet')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "7aa178c1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Brac', 'kuet', 'ewu', 'nsu', 'buet']"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "uni"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "6652ef8c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Brac', 'kuet', 'ewu', 'nsu', 'buet', 10, 20]"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "uni.extend([10,20])\n",
    "uni"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "3d72574a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Brac', 'kuet', 'ewu', 'nsu', 'buet', 10, 20, 1, 2, 3]"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "uni+num"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "ffeed04c",
   "metadata": {},
   "outputs": [],
   "source": [
    "del uni[7:]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "4432a4a9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Brac', 'kuet', 'ewu', 'nsu', 'buet', 10, 20]"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "uni"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "2ee6fb87",
   "metadata": {},
   "outputs": [],
   "source": [
    "del uni [7:]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "2bf57ae7",
   "metadata": {},
   "outputs": [],
   "source": [
    "uni.remove(20)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "8a728c0c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Brac', 'kuet', 'ewu', 'nsu', 'buet', 10]"
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "uni"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "25690552",
   "metadata": {},
   "outputs": [],
   "source": [
    "del uni [-1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "730b53f8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Brac', 'kuet', 'ewu', 'nsu', 'buet']"
      ]
     },
     "execution_count": 48,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "uni"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "58890c15",
   "metadata": {},
   "outputs": [],
   "source": [
    "del uni[1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "52c8fd35",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Brac', 'ewu', 'nsu', 'buet']"
      ]
     },
     "execution_count": 51,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "uni"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "4ae20ec5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 55,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "uni.count('nsu')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "e9f9e242",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 54,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "uni.count('ewu')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "ba1fe3e4",
   "metadata": {},
   "outputs": [],
   "source": [
    "uni.append('kuet')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "5cf65234",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Brac', 'ewu', 'nsu', 'buet', 'kuet']"
      ]
     },
     "execution_count": 61,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "uni"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "id": "9faba693",
   "metadata": {},
   "outputs": [],
   "source": [
    "uni.insert(0,'buet')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "d41fba3e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['buet', 'Brac', 'ewu', 'nsu', 'buet', 'kuet']"
      ]
     },
     "execution_count": 63,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "uni"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "id": "399ec65e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2"
      ]
     },
     "execution_count": 64,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "uni.count('buet')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "id": "0924300a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[5, 6, 7, 8, 9]"
      ]
     },
     "execution_count": 66,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sort=[9,8,7,5,6]\n",
    "sorted(sort)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b1e1f78f",
   "metadata": {},
   "source": [
    "The count('uni')# question,how to count total number of element in a set"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "id": "ab8487cb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(list, tuple)"
      ]
     },
     "execution_count": 76,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tup=('a','b','c','d')\n",
    "type(uni),type(tup)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "id": "3ead16ec",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "('a', 'b', 'c', 'd')"
      ]
     },
     "execution_count": 77,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tup+('e',)\n",
    "tup"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "id": "d0e5d9ae",
   "metadata": {},
   "outputs": [],
   "source": [
    "tup=tup+('e',)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "id": "3a807804",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "('a', 'b', 'c', 'd', 'e')"
      ]
     },
     "execution_count": 79,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tup"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "id": "d46d7c51",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "6"
      ]
     },
     "execution_count": 80,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(uni)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "id": "edb61f3b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5"
      ]
     },
     "execution_count": 81,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(tup)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "id": "2f1a6598",
   "metadata": {},
   "outputs": [],
   "source": [
    "dict={'b':'buet','k':'kuet','e':'ewu'}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "id": "e288c7db",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'ewu'"
      ]
     },
     "execution_count": 90,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dict['e']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "id": "55c93e26",
   "metadata": {},
   "outputs": [],
   "source": [
    "dict['r']='ruet'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "id": "c8f2bb18",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'b': 'buet', 'k': 'kuet', 'e': 'ewu', 'r': 'ruet'}"
      ]
     },
     "execution_count": 93,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dict"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "id": "3869f9ee",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dict_values(['buet', 'kuet', 'ewu', 'ruet'])"
      ]
     },
     "execution_count": 96,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    " dict.values()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "id": "ffe059f2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "4"
      ]
     },
     "execution_count": 97,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(dict)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 98,
   "id": "13337312",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{4, 5, 8, 9}"
      ]
     },
     "execution_count": 98,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s={4,4,5,8,9}\n",
    "set(s)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1ea756b2",
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.10.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
