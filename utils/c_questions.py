#! /usr/bin/env python

__author__ = "virtuoso.irfan@gmail.com(Muhammad Irfan)"

import io
import sys

STDOUT = io.open(1, mode="wt", encoding="utf-8", closefd=False)

STATIC_QUESTIONS = r"""QS "C-Syl_Vowel==x"      {|x/C:}
QS "C-Syl_Vowel==no"    {|novowel/C:}
QS "L-Word_GPOS==0"     {/D:0_}
QS "L-Word_GPOS==aux"   {/D:aux_}
QS "L-Word_GPOS==cc"    {/D:cc_}
QS "L-Word_GPOS==content" {/D:content_}
QS "L-Word_GPOS==det"   {/D:det_}
QS "L-Word_GPOS==in"    {/D:in_}
QS "L-Word_GPOS==md"    {/D:md_}
QS "L-Word_GPOS==pps"   {/D:pps_}
QS "L-Word_GPOS==punc"    {/D:punc_}
QS "L-Word_GPOS==to"    {/D:to_}
QS "L-Word_GPOS==wp"    {/D:wp_}
QS "C-Word_GPOS==x"   {/E:x+}
QS "C-Word_GPOS==aux"   {/E:aux+}
QS "C-Word_GPOS==cc"    {/E:cc+}
QS "C-Word_GPOS==content" {/E:content+}
QS "C-Word_GPOS==det"   {/E:det+}
QS "C-Word_GPOS==in"    {/E:in+}
QS "C-Word_GPOS==md"    {/E:md+}
QS "C-Word_GPOS==pps"   {/E:pps+}
QS "C-Word_GPOS==punc"    {/E:punc+}
QS "C-Word_GPOS==to"    {/E:to+}
QS "C-Word_GPOS==wp"    {/E:wp+}
QS "R-Word_GPOS==0"     {/F:0_}
QS "R-Word_GPOS==aux"   {/F:aux_}
QS "R-Word_GPOS==cc"    {/F:cc_}
QS "R-Word_GPOS==content" {/F:content_}
QS "R-Word_GPOS==det"   {/F:det_}
QS "R-Word_GPOS==in"    {/F:in_}
QS "R-Word_GPOS==md"    {/F:md_}
QS "R-Word_GPOS==pps"   {/F:pps_}
QS "R-Word_GPOS==punc"    {/F:punc_}
QS "R-Word_GPOS==to"    {/F:to_}
QS "R-Word_GPOS==wp"    {/F:wp_}
CQS "Seg_Fw"                                      {@(\d+)_}
CQS "Seg_Bw"                                      {_(\d+)/A:}
CQS "L-Syl_Stress"                                {/A:(\d+)_}
CQS "L-Syl_Accent"                                {_(\d+)_}
CQS "L-Syl_Num-Segs"                              {_(\d+)/B:}
CQS "C-Syl_Stress"                                {/B:(\d+)-}
CQS "C-Syl_Accent"                                {-(\d+)-}
CQS "C-Syl_Num-Segs"                              {-(\d+)@}
CQS "Pos_C-Syl_in_C-Word(Fw)"                     {@(\d+)-}
CQS "Pos_C-Syl_in_C-Word(Bw)"                     {-(\d+)&}
CQS "Pos_C-Syl_in_C-Phrase(Fw)"                     {&(\d+)-}
CQS "Pos_C-Syl_in_C-Phrase(Bw)"                     {-(\d+)#}
CQS "Num-StressedSyl_before_C-Syl_in_C-Phrase"      {#(\d+)-}
CQS "Num-StressedSyl_after_C-Syl_in_C-Phrase"   {-(\d+)$}
CQS "Num-AccentedSyl_before_C-Syl_in_C-Phrase"      {$(\d+)-}
CQS "Num-AccentedSyl_after_C-Syl_in_C-Phrase"     {-(\d+)!}
CQS "Num-Syl_from_prev-StressedSyl"               {!(\d+)-}
CQS "Num-Syl_from_next-StressedSyl"                 {-(\d+);}
CQS "Num-Syl_from_prev-AccentedSyl"                 {;(\d+)-}
CQS "Num-Syl_from_next-AccentedSyl"                 {-(\d+)|}
CQS "R-Syl_Stress"                                {/C:(\d+)+}
CQS "R-Syl_Accent"                                {+(\d+)+}
CQS "R-Syl_Num-Segs"                              {+(\d+)/D:}
CQS "L-Word_Num-Syls"                             {_(\d+)/E:}
CQS "C-Word_Num-Syls"                             {+(\d+)@}
CQS "Pos_C-Word_in_C-Phrase(Fw)"                  {@(\d+)+}
CQS "Pos_C-Word_in_C-Phrase(Bw)"                  {+(\d+)&}
CQS "Num-ContWord_before_C-Word_in_C-Phrase"      {&(\d+)+}
CQS "Num-ContWord_after_C-Word_in_C-Phrase"         {+(\d+)#}
CQS "Num-Words_from_prev-ContWord"                  {#(\d+)+}
CQS "Num-Words_from_next-ContWord"                  {+(\d+)/F:}
CQS "R-Word_Num-Syls"                             {_(\d+)/G:}
CQS "L-Phrase_Num-Syls"                             {/G:(\d+)_}
CQS "L-Phrase_Num-Words"                          {_(\d+)/H:}
CQS "C-Phrase_Num-Syls"                             {/H:(\d+)=}
CQS "C-Phrase_Num-Words"                          {=(\d+)@}
CQS "Pos_C-Phrase_in_Utterance(Fw)"                 {@(\d+)=}
CQS "Pos_C-Phrase_in_Utterance(Bw)"                 {=(\d+)&}
CQS "R-Phrase_Num-Syls"                             {/I:(\d+)=}
CQS "R-Phrase_Num-Words"                          {=(\d+)/J:}
CQS "Num-Syls_in_Utterance"                         {/J:(\d+)+}
CQS "Num-Words_in_Utterance"                      {+(\d+)-}
CQS "Num-Phrases_in_Utterance"                    {-(\d+)}
"""

NASAL_VOWEL_QUESTIONS = [["C-Nasal_Vowel", "*-%s?+*"]]
SIMPLE_FINAL_QUESTIONS = [["C-Simple_Vowel", "*-%s?+*"]]
COMPOUND_FINAL_QUESTIONS = [["C-Compound_Vowel", "*-%s?+*"]]

ANTERIOR_NASAL_VOWEL_QUESTIONS = [["C-Anterior_Nasal_Vowel", "*-%s?+*"]]
POSTERIOR_NASAL_VOWEL_QUESTIONS = [["C-Posterior_Nasal_Vowel", "*-%s?+*"]]

TYPEA_QUESTIONS = [["C-TypeA", "*-%s?+*"]]
TYPEE_QUESTIONS = [["C-TypeE", "*-%s?+*"]]
TYPEI_QUESTIONS = [["C-TypeI", "*-%s?+*"]]
TYPEO_QUESTIONS = [["C-TypeO", "*-%s?+*"]]
TYPEU_QUESTIONS = [["C-TypeU", "*-%s?+*"]]
TYPEV_QUESTIONS = [["C-TypeV", "*-%s?+*"]]

STOP_QUESTIONS = [["C-Stop", "*-%s+*"]]
ASPIRATED_STOP_QUESTIONS = [["C-Aspirated_Sto", "*-%s+*"]]
UNASPIRATED_STOP_QUESTIONS = [["C-Unaspirated_Stop", "*-%s+*"]]

AFFRICATE_QUESTIONS = [["C-Affricate", "*-%s+*"]]
ASPIRATED_AFFRICATE_QUESTIONS = [["C-Aspirated_Affricate", "*-%s+*"]]
UNASPIRATED_AFFRICATE_QUESTIONS = [["C-Unaspirated_Affricate", "*-%s+*"]]

FRICATIVE_QUESTIONS = [["C-Fricative", "*-%s+*"]]
VOICELESS_FRICATIVE_QUESTIONS = [["C-Voiceless_Fricative", "*-%s+*"]]

NASAL_QUESTIONS = [["C-Nasal", "*-%s+*"]]

LABIAL_QUESTIONS = [["C-Labial", "*-%s+*"]]
LABIAL2_QUESTIONS = [["C-Labial", "*-%s+*"]]

INITIAL_QUESTIONS = [["C-initial", "*-%s+*"]]
FINAL_QUESTIONS = [["C-final", "*-%s+*"]]
SILENCE_QUESTIONS = [["C-silence", "*-%s+*"]]

C_INITIAL_QUESTIONS = [["C", "*-%s+*"]]
C_FINAL_QUESTIONS = [["C", "*-%s?+*"]]

C_SYL_VOWEL_SIMPLE_VOWEL = [["C-Syl-Vowel-Simple_Vowel", "*@%s@*"]]
C_SYL_VOWEL_COMPOUND_VOWEL = [["C-Syl-Vowel-Compound_Vowel", "*@%s@*"]]
C_SYL_VOWEL_NASAL_VOWEL = [["C-Syl-Vowel-Nasal_Vowel", "*@%s@*"]]
C_SYL_VOWEL_ANTERIOR_NASAL_VOWEL = [["C-Syl-Vowel-Anterior_Nasal_Vowel", "*@%s@*"]]
C_SYL_VOWEL_POSTERIOR_NASAL_VOWEL = [["C-Syl-Vowel-Posterior_Nasal_Vowel", "*@%s@*"]]

C_SYL_VOWEL_TYPEA = [["C-Syl-Vowel-TypeA", "*@%s@*"]]
C_SYL_VOWEL_TYPEE = [["C-Syl-Vowel-TypeE", "*@%s@*"]]
C_SYL_VOWEL_TYPEI = [["C-Syl-Vowel-TypeI", "*@%s@*"]]
C_SYL_VOWEL_TYPEO = [["C-Syl-Vowel-TypeO", "*@%s@*"]]
C_SYL_VOWEL_TYPEU = [["C-Syl-Vowel-TypeU", "*@%s@*"]]
C_SYL_VOWEL_TYPEV = [["C-Syl-Vowel-TypeV", "*@%s@*"]]
C_SYL_VOWEL = [["C-Syl-Vowel-", "*@%s@*"]]


C_Syl_Vowel_Simple_Vowel = ["am", "aam", "an", "aan", "em", "im", "in", "on", "ot", "eon", "un", "yun"]
C_Syl_Vowel_Compound_Vowel = ["ang", "aang", "eng", "ing", "ong", "ok", "oeng", "ung"]
C_Syl_Vowel_Nasal_Vowel = ["am", "aam", "an", "aan", "em", "im", "in", "on", "ot", "eon", "un", "yun", "ang", "aang", "eng", "ing",
               "ong", "ok", "oeng", "ung"]
C_Syl_Vowel_Anterior_Nasal_Vowel = ["am", "aam", "an", "aan", "em", "im", "in", "on", "ot", "eon", "un", "yun"]
C_Syl_Vowel_Posterior_Nasal_Vowel = ["ang", "aang", "eng", "ing", "ong", "ok", "oeng", "ung"]

C_Syl_Vowel_TypeA = ["aa", "aai", "aau", "aam", "aan", "aang", "aap", "aat", "aak", "ai", "au", "am", "an", "ang", "ap", "at", "ak"]
C_Syl_Vowel_TypeE = ["e", "eng", "ek", "ei", "eoi", "eon", "eot"]
C_Syl_Vowel_TypeI = ["i", "iu", "im", "in", "ing", "ip", "it", "ik"]
C_Syl_Vowel_TypeO = ["o", "on", "ong", "ot", "ok", "oi", "ou", "oe", "oeng", "oek"]
C_Syl_Vowel_TypeU = ["u", "ui", "un", "ut", "ung", "uk"]
C_Syl_Vowel_TypeV = ["yu", "yun", "yut"]

Stop = ["p", "t", "k", "b", "d", "g"]
Aspirated_Stop = ["p", "t", "k"]
Unaspirated_Stop = ["b", "d", "g"]

Affricate = ["z", "c"]
Aspirated_Affricate = ["c"]
Unaspirated_Affricate = ["z"]

Fricative = ["f", "s", "h"]
Voiceless_Fricative = ["s"]

Nasal = ["m", "n", "ng"]

Labial = ["m", "b", "p"]
Labial2 = ["f"]

Simple_Final = ["am", "aam", "an", "aan", "em", "im", "in", "on", "ot", "eon", "un", "yun"]
Compound_Final = ["ang", "aang", "eng", "ing", "ong", "ok", "oeng", "ung"]

Nasal_Vowel = ["am", "aam", "an", "aan", "em", "im", "in", "on", "ot", "eon", "un", "yun", "ang", "aang", "eng", "ing",
               "ong", "ok", "oeng", "ung"]
Anterior_Nasal_Vowel = ["am", "aam", "an", "aan", "em", "im", "in", "on", "ot", "eon", "un", "yun"]
Posterior_Nasal_Vowel = ["ang", "aang", "eng", "ing", "ong", "ok", "oeng", "ung"]

TypeA = ["aa", "aai", "aau", "aam", "aan", "aang", "aap", "aat", "aak", "ai", "au", "am", "an", "ang", "ap", "at", "ak"]
TypeE = ["e", "eng", "ek", "ei", "eoi", "eon", "eot"]
TypeI = ["i", "iu", "im", "in", "ing", "ip", "it", "ik"]
TypeO = ["o", "on", "ong", "ot", "ok", "oi", "ou", "oe", "oeng", "oek"]
TypeU = ["u", "ui", "un", "ut", "ung", "uk"]
TypeV = ["yu", "yun", "yut"]

initial = ["b", "p", "m", "f", "d", "t", "n", "l", "g", "k", "ng", "h", "gw", "kw", "w", "z", "c", "s", "j"]
final = ["aa", "aai", "aau", "aam", "aan", "aang", "aap", "aat", "aak", "ai", "au", "am", "an", "ang", "ap", "at", "ak",
         "e", "eng", "ek", "ei", "eoi", "eon", "eot", "i", "iu", "im", "in", "ing", "ip", "it", "ik", "o", "on", "ong",
         "ot", "ok", "oi", "ou", "oe", "oeng", "oek", "u", "ui", "un", "ut", "ung", "uk", "yu", "yun", "yut", "ng", "m"]
silence = ["sil", "pau", "sp"]


def main():
    # phonology = json.loads(open(argv[1]).read())
    content = ""
    # Vowel =====================================================================
    nv = []
    for v in Nasal_Vowel:
        nv.append(NASAL_VOWEL_QUESTIONS[0][1] % v)
    nv = ",".join(nv)
    content += "QS \"%s\"\t\t\t\t{%s}\n" % (NASAL_VOWEL_QUESTIONS[0][0], nv)

    sf = []
    for v in Simple_Final:
        sf.append(SIMPLE_FINAL_QUESTIONS[0][1] % v)
    sf = ",".join(sf)
    content += "QS \"%s\"\t\t\t\t{%s}\n" % (SIMPLE_FINAL_QUESTIONS[0][0], sf)

    cf = []
    for v in Compound_Final:
        cf.append(COMPOUND_FINAL_QUESTIONS[0][1] % v)
    cf = ",".join(cf)
    content += "QS \"%s\"\t\t\t\t{%s}\n" % (COMPOUND_FINAL_QUESTIONS[0][0], cf)
    anv = []
    for v in Anterior_Nasal_Vowel:
        anv.append(ANTERIOR_NASAL_VOWEL_QUESTIONS[0][1] % v)
    anv = ",".join(anv)
    content += "QS \"%s\"\t\t\t\t{%s}\n" % (ANTERIOR_NASAL_VOWEL_QUESTIONS[0][0], anv)

    pnv = []
    for v in Posterior_Nasal_Vowel:
        pnv.append(POSTERIOR_NASAL_VOWEL_QUESTIONS[0][1] % v)
    pnv = ",".join(pnv)
    content += "QS \"%s\"\t\t\t\t{%s}\n" % (POSTERIOR_NASAL_VOWEL_QUESTIONS[0][0], pnv)

    ta = []
    for v in TypeA:
        ta.append(TYPEA_QUESTIONS[0][1] % v)
    ta = ",".join(ta)
    content += "QS \"%s\"\t\t\t\t{%s}\n" % (TYPEA_QUESTIONS[0][0], ta)

    te = []
    for v in TypeE:
        te.append(TYPEE_QUESTIONS[0][1] % v)
    te = ",".join(te)
    content += "QS \"%s\"\t\t\t\t{%s}\n" % (TYPEE_QUESTIONS[0][0], te)

    ti = []
    for v in TypeI:
        ti.append(TYPEI_QUESTIONS[0][1] % v)
    ti = ",".join(ti)
    content += "QS \"%s\"\t\t\t\t{%s}\n" % (TYPEI_QUESTIONS[0][0], ti)

    tu = []
    for v in TypeU:
        tu.append(TYPEO_QUESTIONS[0][1] % v)
    tu = ",".join(tu)
    content += "QS \"%s\"\t\t\t\t{%s}\n" % (TYPEO_QUESTIONS[0][0], tu)

    tv = []
    for v in TypeU:
        tv.append(TYPEO_QUESTIONS[0][1] % v)
    tv = ",".join(tv)
    content += "QS \"%s\"\t\t\t\t{%s}\n" % (TYPEO_QUESTIONS[0][0], tv)
    # STOP ======================================================================
    s = []
    for v in Stop:
        s.append(STOP_QUESTIONS[0][1] % v)
    s = ",".join(s)
    content += "QS \"%s\"\t\t\t\t{%s}\n" % (STOP_QUESTIONS[0][0], s)

    asp = []
    for v in Aspirated_Stop:
        asp.append(ASPIRATED_STOP_QUESTIONS[0][1] % v)
    asp = ",".join(asp)
    content += "QS \"%s\"\t\t\t\t{%s}\n" % (ASPIRATED_STOP_QUESTIONS[0][0], asp)

    unp = []
    for v in Unaspirated_Stop:
        unp.append(UNASPIRATED_STOP_QUESTIONS[0][1] % v)
    unp = ",".join(unp)
    content += "QS \"%s\"\t\t\t\t{%s}\n" % (UNASPIRATED_STOP_QUESTIONS[0][0], unp)
    # AFFRICATE ==================================================================
    af = []
    for v in Affricate:
        af.append(AFFRICATE_QUESTIONS[0][1] % v)
    af = ",".join(af)
    content += "QS \"%s\"\t\t\t\t{%s}\n" % (AFFRICATE_QUESTIONS[0][0], af)
    asp = []
    for v in Aspirated_Affricate:
        asp.append(ASPIRATED_AFFRICATE_QUESTIONS[0][1] % v)
    asp = ",".join(asp)
    content += "QS \"%s\"\t\t\t\t{%s}\n" % (ASPIRATED_AFFRICATE_QUESTIONS[0][0], asp)

    unp = []
    for v in Unaspirated_Affricate:
        unp.append(UNASPIRATED_AFFRICATE_QUESTIONS[0][1] % v)
    unp = ",".join(unp)
    content += "QS \"%s\"\t\t\t\t{%s}\n" % (UNASPIRATED_AFFRICATE_QUESTIONS[0][0], unp)
    # Fricative ==================================================================
    f = []
    for v in Fricative:
        f.append(FRICATIVE_QUESTIONS[0][1] % v)
    f = ",".join(f)
    content += "QS \"%s\"\t\t\t\t{%s}\n" % (FRICATIVE_QUESTIONS[0][0], f)
    vf = []
    for v in Fricative:
        vf.append(VOICELESS_FRICATIVE_QUESTIONS[0][1] % v)
    vf = ",".join(vf)
    content += "QS \"%s\"\t\t\t\t{%s}\n" % (VOICELESS_FRICATIVE_QUESTIONS[0][0], vf)
    # Nasal ==================================================================
    n = []
    for v in Nasal:
        n.append(NASAL_QUESTIONS[0][1] % v)
    n = ",".join(n)
    content += "QS \"%s\"\t\t\t\t{%s}\n" % (NASAL_QUESTIONS[0][0], n)
    # Labial ==================================================================
    l = []
    for v in Labial:
        l.append(LABIAL_QUESTIONS[0][1] % v)
    l = ",".join(l)
    content += "QS \"%s\"\t\t\t\t{%s}\n" % (LABIAL_QUESTIONS[0][0], l)

    l2 = []
    for v in Labial2:
        l2.append(LABIAL2_QUESTIONS[0][1] % v)
    l2 = ",".join(l2)
    content += "QS \"%s\"\t\t\t\t{%s}\n" % (LABIAL2_QUESTIONS[0][0], l2)

    i = []
    for v in initial:
        i.append(INITIAL_QUESTIONS[0][1] % v)
    i = ",".join(i)
    content += "QS \"%s\"\t\t\t\t{%s}\n" % (INITIAL_QUESTIONS[0][0], i)

    f = []
    for v in final:
        f.append(FINAL_QUESTIONS[0][1] % v)
    f = ",".join(f)
    content += "QS \"%s\"\t\t\t\t{%s}\n" % (FINAL_QUESTIONS[0][0], f)

    s = []
    for v in silence:
        s.append(SILENCE_QUESTIONS[0][1] % v)
    s = ",".join(s)
    content += "QS \"%s\"\t\t\t\t{%s}\n" % (SILENCE_QUESTIONS[0][0], s)
    # C questions ==================================================================
    for v in initial:
        k = C_INITIAL_QUESTIONS[0][1] % v
        content += "QS \"%s-%s\"\t\t\t\t{%s}\n" % (C_INITIAL_QUESTIONS[0][0], v, k)
    for v in final:
        k = C_FINAL_QUESTIONS[0][1] % v
        content += "QS \"%s-%s\"\t\t\t\t{%s}\n" % (C_FINAL_QUESTIONS[0][0], v, k)
    for v in silence:
        k = SILENCE_QUESTIONS[0][1] % v
        content += "QS \"C-%s\"\t\t\t\t{%s}\n" % (v, k)

    # C  ==================================================================
    s = []
    for v in C_Syl_Vowel_Simple_Vowel:
        s.append(C_SYL_VOWEL_SIMPLE_VOWEL[0][1] % v)
    s = ",".join(s)
    content += "QS \"%s\"\t\t\t\t{%s}\n" % (C_SYL_VOWEL_SIMPLE_VOWEL[0][0], s)

    s = []
    for v in C_Syl_Vowel_Compound_Vowel:
        s.append(C_SYL_VOWEL_COMPOUND_VOWEL[0][1] % v)
    s = ",".join(s)
    content += "QS \"%s\"\t\t\t\t{%s}\n" % (C_SYL_VOWEL_COMPOUND_VOWEL[0][0], s)
    s = []
    for v in C_Syl_Vowel_Nasal_Vowel:
        s.append(C_SYL_VOWEL_NASAL_VOWEL[0][1] % v)
    s = ",".join(s)
    content += "QS \"%s\"\t\t\t\t{%s}\n" % (C_SYL_VOWEL_NASAL_VOWEL[0][0], s)

    s = []
    for v in C_Syl_Vowel_Anterior_Nasal_Vowel:
        s.append(C_SYL_VOWEL_ANTERIOR_NASAL_VOWEL[0][1] % v)
    s = ",".join(s)
    content += "QS \"%s\"\t\t\t\t{%s}\n" % (C_SYL_VOWEL_ANTERIOR_NASAL_VOWEL[0][0], s)
    s = []
    for v in C_Syl_Vowel_Posterior_Nasal_Vowel:
        s.append(C_SYL_VOWEL_POSTERIOR_NASAL_VOWEL[0][1] % v)
    s = ",".join(s)
    content += "QS \"%s\"\t\t\t\t{%s}\n" % (C_SYL_VOWEL_POSTERIOR_NASAL_VOWEL[0][0], s)

    s = []
    for v in C_Syl_Vowel_TypeA:
        s.append(C_SYL_VOWEL_TYPEA[0][1] % v)
    s = ",".join(s)
    content += "QS \"%s\"\t\t\t\t{%s}\n" % (C_SYL_VOWEL_TYPEA[0][0], s)

    s = []
    for v in C_Syl_Vowel_TypeE:
        s.append(C_SYL_VOWEL_TYPEE[0][1] % v)
    s = ",".join(s)
    content += "QS \"%s\"\t\t\t\t{%s}\n" % (C_SYL_VOWEL_TYPEE[0][0], s)

    s = []
    for v in C_Syl_Vowel_TypeI:
        s.append(C_SYL_VOWEL_TYPEI[0][1] % v)
    s = ",".join(s)
    content += "QS \"%s\"\t\t\t\t{%s}\n" % (C_SYL_VOWEL_TYPEI[0][0], s)

    s = []
    for v in C_Syl_Vowel_TypeO:
        s.append(C_SYL_VOWEL_TYPEO[0][1] % v)
    s = ",".join(s)
    content += "QS \"%s\"\t\t\t\t{%s}\n" % (C_SYL_VOWEL_TYPEO[0][0], s)

    s = []
    for v in C_Syl_Vowel_TypeU:
        s.append(C_SYL_VOWEL_TYPEE[0][1] % v)
    s = ",".join(s)
    content += "QS \"%s\"\t\t\t\t{%s}\n" % (C_SYL_VOWEL_TYPEU[0][0], s)

    s = []
    for v in C_Syl_Vowel_TypeV:
        s.append(C_SYL_VOWEL_TYPEE[0][1] % v)
    s = ",".join(s)
    content += "QS \"%s\"\t\t\t\t{%s}\n" % (C_SYL_VOWEL_TYPEV[0][0], s)

    for v in Simple_Final:
        k = C_SYL_VOWEL[0][1] % v
        content += "QS \"%s%s\"\t\t\t\t{%s}\n" % (C_SYL_VOWEL[0][0], v, k)

    for v in Compound_Final:
        k = C_SYL_VOWEL[0][1] % v
        content += "QS \"%s%s\"\t\t\t\t{%s}\n" % (C_SYL_VOWEL[0][0], v, k)

    for v in Nasal_Vowel:
        k = C_SYL_VOWEL[0][1] % v
        content += "QS \"%s%s\"\t\t\t\t{%s}\n" % (C_SYL_VOWEL[0][0], v, k)

    print(content)


if __name__ == "__main__":
    main()
