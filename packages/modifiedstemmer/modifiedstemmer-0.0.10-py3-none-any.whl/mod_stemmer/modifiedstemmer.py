#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
#######################################################
# Modified version of porter stemmer by Vivake Gupta (v@nano.com)       
# Author: Abhinav Kumar                               #
# Email: anu55abhi@gmail.com                          #
# Last modified: 22/Oct/2024                          #
#                                                     #
# Usage:                                              #
# Import it, instantiate it, and pass                 #
# words as arguments to the stem method.              #
#                                                     #                 
#######################################################


class stemmer(object):
    """
    Stem words according to the Porter stemming algorithm.
    """

    def __init__(self):
        self.buffer = ""  # buffer for word to be stemmed
        self.end = 0
        self.start = 0
        self.j = 0   # j is a general offset into the string

    def is_consonant(self, index):
        """is_consonant(index) is TRUE <=> buffer[index] is a consonant."""
        if self.buffer[index] in 'aeiou':
            return False
        if self.buffer[index] == 'y':
            if index == self.start:
                return True
            else:
                return not self.is_consonant(index - 1)
        return True

    def measure_consonant_sequences(self):
        """measure_consonant_sequences() measures the number of consonant sequences between start and j."""
        n = 0
        index = self.start
        while True:
            if index > self.j:
                return n
            if not self.is_consonant(index):
                break
            index += 1
        index += 1
        while True:
            while True:
                if index > self.j:
                    return n
                if self.is_consonant(index):
                    break
                index += 1
            index += 1
            n += 1
            while True:
                if index > self.j:
                    return n
                if not self.is_consonant(index):
                    break
                index += 1
            index += 1

    def contains_vowel(self):
        """contains_vowel() is TRUE <=> start,...j contains a vowel"""
        for index in range(self.start, self.j + 1):
            if not self.is_consonant(index):
                return True
        return False

    def ends_double_consonant(self, j):
        """ends_double_consonant(j) is TRUE <=> j,(j-1) contain a double consonant."""
        if j < (self.start + 1):
            return False
        if self.buffer[j] != self.buffer[j-1]:
            return False
        return self.is_consonant(j)

    def cvc(self, index):
        """cvc(index) is TRUE <=> index-2,index-1,index has the form consonant - vowel - consonant
        and also if the second c is not w,x or y. this is used when trying to
        restore an e at the end of a short  e.g.

           cav(e), lov(e), hop(e), crim(e), but
           snow, box, tray.
        """
        if index < (self.start + 2) or not self.is_consonant(index) or self.is_consonant(index-1) or not self.is_consonant(index-2):
            return False
        ch = self.buffer[index]
        if ch in 'wxy':
            return False
        return True

    def ends_with(self, s):
        """ends_with(s) is TRUE <=> start,...end ends with the string s."""
        length = len(s)
        if s[length - 1] != self.buffer[self.end]:  # tiny speed-up
            return False
        if length > (self.end - self.start + 1):
            return False
        if self.buffer[self.end-length+1:self.end+1] != s:
            return False
        self.j = self.end - length
        return True

    def set_to(self, s):
        """set_to(s) sets (j+1),...end to the characters in the string s, readjusting end."""
        length = len(s)
        self.buffer = self.buffer[:self.j+1] + s + self.buffer[self.j+length+1:]
        self.end = self.j + length

    def replace_if_measure_gt_zero(self, s):
        """replace_if_measure_gt_zero(s) is used further down."""
        if self.measure_consonant_sequences() > 0:
            self.set_to(s)

    def remove_plural_and_ed_or_ing(self):
        """remove_plural_and_ed_or_ing() gets rid of plurals and -ed or -ing. e.g.
           caresses  ->  caress
           ponies    ->  poni
           ties      ->  ti
           caress    ->  caress
           cats      ->  cat
           feed      ->  feed
           agreed    ->  agree
           disabled  ->  disable
           matting   ->  mat
           mating    ->  mate
           meeting   ->  meet
           milling   ->  mill
           messing   ->  mess
           meetings  ->  meet
        """
        if self.buffer[self.end] == 's':
            if self.ends_with("sses"):
                self.end = self.end - 2
            elif self.ends_with("ies"):
                self.set_to("i")
            elif self.buffer[self.end - 1] != 's':
                self.end = self.end - 1
        if self.ends_with("eed"):
            if self.measure_consonant_sequences() > 0:
                self.end = self.end - 1
        elif (self.ends_with("ed") or self.ends_with("ing")) and self.contains_vowel():
            self.end = self.j
            if self.ends_with("at"):   self.set_to("ate")
            elif self.ends_with("bl"): self.set_to("ble")
            elif self.ends_with("iz"): self.set_to("ize")
            elif self.ends_double_consonant(self.end):
                self.end = self.end - 1
                ch = self.buffer[self.end]
                if ch in 'lsz':
                    self.end = self.end + 1
            elif (self.measure_consonant_sequences() == 1 and self.cvc(self.end)):
                self.set_to("e")

    def replace_y_with_i_if_in_stem(self):
        """replace_y_with_i_if_in_stem() turns terminal y to i when there is another vowel in the stem."""
        if self.ends_with("y") and self.contains_vowel():
            self.buffer = self.buffer[:self.end] + 'i' + self.buffer[self.end+1:]

    def map_double_suffixes_to_single(self):
        """map_double_suffixes_to_single() maps double suffices to single ones.
        so -ization ( = -ize plus -ation) maps to -ize etc. note that the
        string before the suffix must give measure_consonant_sequences() > 0.
        """
        if self.buffer[self.end - 1] == 'a':
            if self.ends_with("ational"):   self.replace_if_measure_gt_zero("ate")
            elif self.ends_with("tional"):  self.replace_if_measure_gt_zero("tion")
        elif self.buffer[self.end - 1] == 'c':
            if self.ends_with("enci"):      self.replace_if_measure_gt_zero("ence")
            elif self.ends_with("anci"):    self.replace_if_measure_gt_zero("ance")
        elif self.buffer[self.end - 1] == 'e':
            if self.ends_with("izer"):      self.replace_if_measure_gt_zero("ize")
        elif self.buffer[self.end - 1] == 'l':
            if self.ends_with("bli"):       self.replace_if_measure_gt_zero("ble")  # --DEPARTURE--
            # To match the published algorithm, replace this phrase with
            #   if self.ends_with("abli"):      self.replace_if_measure_gt_zero("able")
            elif self.ends_with("alli"):    self.replace_if_measure_gt_zero("al")
            elif self.ends_with("entli"):   self.replace_if_measure_gt_zero("ent")
            elif self.ends_with("eli"):     self.replace_if_measure_gt_zero("e")
            elif self.ends_with("ousli"):   self.replace_if_measure_gt_zero("ous")
        elif self.buffer[self.end - 1] == 'o':
            if self.ends_with("ization"):   self.replace_if_measure_gt_zero("ize")
            elif self.ends_with("ation"):   self.replace_if_measure_gt_zero("ate")
            elif self.ends_with("ator"):    self.replace_if_measure_gt_zero("ate")
        elif self.buffer[self.end - 1] == 's':
            if self.ends_with("alism"):     self.replace_if_measure_gt_zero("al")
            elif self.ends_with("iveness"): self.replace_if_measure_gt_zero("ive")
            elif self.ends_with("fulness"): self.replace_if_measure_gt_zero("ful")
            elif self.ends_with("ousness"): self.replace_if_measure_gt_zero("ous")
        elif self.buffer[self.end - 1] == 't':
            if self.ends_with("aliti"):     self.replace_if_measure_gt_zero("al")
            elif self.ends_with("iviti"):   self.replace_if_measure_gt_zero("ive")
            elif self.ends_with("biliti"):  self.replace_if_measure_gt_zero("ble")
        elif self.buffer[self.end - 1] == 'g':  # --DEPARTURE--
            if self.ends_with("logi"):      self.replace_if_measure_gt_zero("log")
        # To match the published algorithm, delete this phrase

    def handle_special_suffixes(self):
        """handle_special_suffixes() deals with -ic-, -full, -ness etc. similar strategy to map_double_suffixes_to_single."""
        if self.buffer[self.end] == 'e':
            if self.ends_with("icate"):     self.replace_if_measure_gt_zero("ic")
            elif self.ends_with("ative"):   self.replace_if_measure_gt_zero("")
            elif self.ends_with("alize"):   self.replace_if_measure_gt_zero("al")
        elif self.buffer[self.end] == 'i':
            if self.ends_with("iciti"):     self.replace_if_measure_gt_zero("ic")
        elif self.buffer[self.end] == 'l':
            if self.ends_with("ical"):      self.replace_if_measure_gt_zero("ic")
            elif self.ends_with("ful"):     self.replace_if_measure_gt_zero("")
        elif self.buffer[self.end] == 's':
            if self.ends_with("ness"):      self.replace_if_measure_gt_zero("")

    def handle_suffixes(self):
        """handle_suffixes() takes off -ant, -ence etc., in context <c>vcvc<v>."""
        if self.buffer[self.end - 1] == 'a':
            if self.ends_with("al"):
                pass
            else:
                return
        elif self.buffer[self.end - 1] == 'c':
            if self.ends_with("ance") or self.ends_with("ence"):
                pass
            else:
                return
        elif self.buffer[self.end - 1] == 'e':
            if self.ends_with("er"):
                pass
            else:
                return
        elif self.buffer[self.end - 1] == 'i':
            if self.ends_with("ic"):
                pass
            else:
                return
        elif self.buffer[self.end - 1] == 'l':
            if self.ends_with("able") or self.ends_with("ible"):
                pass
            else:
                return
        elif self.buffer[self.end - 1] == 'n':
            if self.ends_with("ant") or self.ends_with("ement") or self.ends_with("ment") or self.ends_with("ent"):
                pass
            else:
                return
        elif self.buffer[self.end - 1] == 'o':
            if (self.ends_with("ion") and (self.buffer[self.j] == 's' or self.buffer[self.j] == 't')) or self.ends_with("ou"):
                pass
            else:
                return
        elif self.buffer[self.end - 1] == 's':
            if self.ends_with("ism"):
                pass
            else:
                return
        elif self.buffer[self.end - 1] == 't':
            if self.ends_with("ate") or self.ends_with("iti"):
                pass
            else:
                return
        elif self.buffer[self.end - 1] == 'u':
            if self.ends_with("ous"):
                pass
            else:
                return
        elif self.buffer[self.end - 1] == 'v':
            if self.ends_with("ive"):
                pass
            else:
                return
        elif self.buffer[self.end - 1] == 'z':
            if self.ends_with("ize"):
                pass
            else:
                return
        else:
            return
        if self.measure_consonant_sequences() > 1:
            self.end = self.j

    def finalize_stemming(self):
        """finalize_stemming() removes a final -e if measure_consonant_sequences() > 1, and changes -ll to -l if
        measure_consonant_sequences() > 1.
        """
        self.j = self.end
        if self.buffer[self.end] == 'e':
            a = self.measure_consonant_sequences()
            if a > 1 or (a == 1 and not self.cvc(self.end - 1)):
                self.end = self.end - 1
        if self.buffer[self.end] == 'l' and self.ends_double_consonant(self.end) and self.measure_consonant_sequences() > 1:
            self.end = self.end - 1

    def handle_verb_suffixes(self):
        """handle_verb_suffixes() handles verb suffixes and other additional rules."""
        if self.ends_with("ing") and self.contains_vowel():
            self.set_to("e")
        elif self.ends_with("ed") and self.contains_vowel():
            self.set_to("")
        elif self.ends_with("es") and self.measure_consonant_sequences() > 0:
            self.set_to("e")
        elif self.ends_with("s") and self.measure_consonant_sequences() > 1:
            self.set_to("")
        elif self.ends_with("ational"):
            self.replace_if_measure_gt_zero("ate")
        elif self.ends_with("tional"):
            self.replace_if_measure_gt_zero("tion")
        elif self.ends_with("ing"):
            self.set_to("")

    def stem(self, word):
        """Stem the word if it has more than two characters, otherwise return it as is."""
        if len(word) <= 2:
            return word
        else:
            # copy the parameters into statics
            self.buffer = word
            self.end = len(word) - 1
            self.start = 0

            self.remove_plural_and_ed_or_ing()
            self.replace_y_with_i_if_in_stem()
            self.map_double_suffixes_to_single()
            self.handle_special_suffixes()
            self.handle_suffixes()
            self.finalize_stemming()
            self.handle_verb_suffixes()  # Added step

            return self.buffer[self.start:self.end + 1]
