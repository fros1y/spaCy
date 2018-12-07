# coding: utf8
from __future__ import unicode_literals

from ...symbols import ORTH, LEMMA, TAG, NORM, PRON_LEMMA


_exc = {}
_exclude = ["Ill", "ill", "Its", "its", "Hell", "hell", "Shell", "shell",
               "Shed", "shed", "were", "Were", "Well", "well", "Whore", "whore"]


# Pronouns

for pron in ["i"]:
    for orth in [pron, pron.title()]:
        _exc[orth + "'m"] = [
            {ORTH: orth, LEMMA: PRON_LEMMA, NORM: pron, TAG: "PRP"},
            {ORTH: "'m", LEMMA: "be", NORM: "am", TAG: "VBP", "tenspect": 1, "number": 1}]

        _exc[orth + "m"] = [
            {ORTH: orth, LEMMA: PRON_LEMMA, NORM: pron, TAG: "PRP"},
            {ORTH: "m", LEMMA: "be", TAG: "VBP", "tenspect": 1, "number": 1 }]

        _exc[orth + "'ma"] = [
            {ORTH: orth, LEMMA: PRON_LEMMA, NORM: pron, TAG: "PRP"},
            {ORTH: "'m", LEMMA: "be", NORM: "am"},
            {ORTH: "a", LEMMA: "going to", NORM: "gonna"}]

        _exc[orth + "ma"] = [
            {ORTH: orth, LEMMA: PRON_LEMMA, NORM: pron, TAG: "PRP"},
            {ORTH: "m", LEMMA: "be", NORM: "am"},
            {ORTH: "a", LEMMA: "going to", NORM: "gonna"}]


for pron in ["i", "you", "he", "she", "it", "we", "they"]:
    for orth in [pron, pron.title()]:
        _exc[orth + "'ll"] = [
            {ORTH: orth, LEMMA: PRON_LEMMA, NORM: pron, TAG: "PRP"},
            {ORTH: "'ll", LEMMA: "will", NORM: "will", TAG: "MD"}]

        _exc[orth + "ll"] = [
            {ORTH: orth, LEMMA: PRON_LEMMA, NORM: pron, TAG: "PRP"},
            {ORTH: "ll", LEMMA: "will", NORM: "will", TAG: "MD"}]

        _exc[orth + "'ll've"] = [
            {ORTH: orth, LEMMA: PRON_LEMMA, NORM: pron, TAG: "PRP"},
            {ORTH: "'ll", LEMMA: "will", NORM: "will", TAG: "MD"},
            {ORTH: "'ve", LEMMA: "have", NORM: "have", TAG: "VB"}]

        _exc[orth + "llve"] = [
            {ORTH: orth, LEMMA: PRON_LEMMA, NORM: pron, TAG: "PRP"},
            {ORTH: "ll", LEMMA: "will", NORM: "will", TAG: "MD"},
            {ORTH: "ve", LEMMA: "have", NORM: "have", TAG: "VB"}]

        _exc[orth + "'d"] = [
            {ORTH: orth, LEMMA: PRON_LEMMA, NORM: pron, TAG: "PRP"},
            {ORTH: "'d", LEMMA: "would", NORM: "would", TAG: "MD"}]

        _exc[orth + "d"] = [
            {ORTH: orth, LEMMA: PRON_LEMMA, NORM: pron, TAG: "PRP"},
            {ORTH: "d", LEMMA: "would", NORM: "would", TAG: "MD"}]

        _exc[orth + "'d've"] = [
            {ORTH: orth, LEMMA: PRON_LEMMA, NORM: pron, TAG: "PRP"},
            {ORTH: "'d", LEMMA: "would", NORM: "would", TAG: "MD"},
            {ORTH: "'ve", LEMMA: "have", NORM: "have", TAG: "VB"}]

        _exc[orth + "dve"] = [
            {ORTH: orth, LEMMA: PRON_LEMMA, NORM: pron, TAG: "PRP"},
            {ORTH: "d", LEMMA: "would", NORM: "would", TAG: "MD"},
            {ORTH: "ve", LEMMA: "have", NORM: "have", TAG: "VB"}]


for pron in ["i", "you", "we", "they"]:
    for orth in [pron, pron.title()]:
        _exc[orth + "'ve"] = [
            {ORTH: orth, LEMMA: PRON_LEMMA, NORM: pron, TAG: "PRP"},
            {ORTH: "'ve", LEMMA: "have", NORM: "have", TAG: "VB"}]

        _exc[orth + "ve"] = [
            {ORTH: orth, LEMMA: PRON_LEMMA, NORM: pron, TAG: "PRP"},
            {ORTH: "ve", LEMMA: "have", NORM: "have", TAG: "VB"}]


for pron in ["you", "we", "they"]:
    for orth in [pron, pron.title()]:
        _exc[orth + "'re"] = [
            {ORTH: orth, LEMMA: PRON_LEMMA, NORM: pron, TAG: "PRP"},
            {ORTH: "'re", LEMMA: "be", NORM: "are"}]

        _exc[orth + "re"] = [
            {ORTH: orth, LEMMA: PRON_LEMMA, NORM: pron, TAG: "PRP"},
            {ORTH: "re", LEMMA: "be", NORM: "are", TAG: "VBZ"}]


for pron in ["he", "she", "it"]:
    for orth in [pron, pron.title()]:
        _exc[orth + "'s"] = [
            {ORTH: orth, LEMMA: PRON_LEMMA, NORM: pron, TAG: "PRP"},
            {ORTH: "'s", NORM: "'s"}]

        _exc[orth + "s"] = [
            {ORTH: orth, LEMMA: PRON_LEMMA, NORM: pron, TAG: "PRP"},
            {ORTH: "s"}]


# W-words, relative pronouns, prepositions etc.

for word in ["who", "what", "when", "where", "why", "how", "there", "that"]:
    for orth in [word, word.title()]:
        _exc[orth + "'s"] = [
            {ORTH: orth, LEMMA: word, NORM: word},
            {ORTH: "'s", NORM: "'s"}]

        _exc[orth + "s"] = [
            {ORTH: orth, LEMMA: word, NORM: word},
            {ORTH: "s"}]

        _exc[orth + "'ll"] = [
            {ORTH: orth, LEMMA: word, NORM: word},
            {ORTH: "'ll", LEMMA: "will", NORM: "will", TAG: "MD"}]

        _exc[orth + "ll"] = [
            {ORTH: orth, LEMMA: word, NORM: word},
            {ORTH: "ll", LEMMA: "will", NORM: "will", TAG: "MD"}]

        _exc[orth + "'ll've"] = [
            {ORTH: orth, LEMMA: word, NORM: word},
            {ORTH: "'ll", LEMMA: "will", NORM: "will", TAG: "MD"},
            {ORTH: "'ve", LEMMA: "have", NORM: "have", TAG: "VB"}]

        _exc[orth + "llve"] = [
            {ORTH: orth, LEMMA: word, NORM: word},
            {ORTH: "ll", LEMMA: "will", NORM: "will", TAG: "MD"},
            {ORTH: "ve", LEMMA: "have", NORM: "have", TAG: "VB"}]

        _exc[orth + "'re"] = [
            {ORTH: orth, LEMMA: word, NORM: word},
            {ORTH: "'re", LEMMA: "be", NORM: "are"}]

        _exc[orth + "re"] = [
            {ORTH: orth, LEMMA: word, NORM: word},
            {ORTH: "re", LEMMA: "be", NORM: "are"}]

        _exc[orth + "'ve"] = [
            {ORTH: orth, LEMMA: word, NORM: word},
            {ORTH: "'ve", LEMMA: "have", TAG: "VB"}]

        _exc[orth + "ve"] = [
            {ORTH: orth, LEMMA: word},
            {ORTH: "ve", LEMMA: "have", NORM: "have", TAG: "VB"}]

        _exc[orth + "'d"] = [
            {ORTH: orth, LEMMA: word, NORM: word},
            {ORTH: "'d", NORM: "'d"}]

        _exc[orth + "d"] = [
            {ORTH: orth, LEMMA: word, NORM: word},
            {ORTH: "d"}]

        _exc[orth + "'d've"] = [
            {ORTH: orth, LEMMA: word, NORM: word},
            {ORTH: "'d", LEMMA: "would", NORM: "would", TAG: "MD"},
            {ORTH: "'ve", LEMMA: "have", NORM: "have", TAG: "VB"}]

        _exc[orth + "dve"] = [
            {ORTH: orth, LEMMA: word, NORM: word},
            {ORTH: "d", LEMMA: "would", NORM: "would", TAG: "MD"},
            {ORTH: "ve", LEMMA: "have", NORM: "have", TAG: "VB"}]


# Verbs

for verb_data in [
    {ORTH: "ca", LEMMA: "can", NORM: "can", TAG: "MD"},
    {ORTH: "could", NORM: "could", TAG: "MD"},
    {ORTH: "do", LEMMA: "do", NORM: "do"},
    {ORTH: "does", LEMMA: "do", NORM: "does"},
    {ORTH: "did", LEMMA: "do", NORM: "do", TAG: "VBD"},
    {ORTH: "had", LEMMA: "have", NORM: "have", TAG: "VBD"},
    {ORTH: "may", NORM: "may", TAG: "MD"},
    {ORTH: "might", NORM: "might", TAG: "MD"},
    {ORTH: "must", NORM: "must", TAG: "MD"},
    {ORTH: "need", NORM: "need"},
    {ORTH: "ought", NORM: "ought", TAG: "MD"},
    {ORTH: "sha", LEMMA: "shall", NORM: "shall", TAG: "MD"},
    {ORTH: "should", NORM: "should", TAG: "MD"},
    {ORTH: "wo", LEMMA: "will", NORM: "will", TAG: "MD"},
    {ORTH: "would", NORM: "would", TAG: "MD"}]:
    verb_data_tc = dict(verb_data)
    verb_data_tc[ORTH] = verb_data_tc[ORTH].title()
    for data in [verb_data, verb_data_tc]:
        _exc[data[ORTH] + "n't"] = [
            dict(data),
            {ORTH: "n't", LEMMA: "not", NORM: "not", TAG: "RB"}]

        _exc[data[ORTH] + "nt"] = [
            dict(data),
            {ORTH: "nt", LEMMA: "not", NORM: "not", TAG: "RB"}]

        _exc[data[ORTH] + "n't've"] = [
            dict(data),
            {ORTH: "n't", LEMMA: "not", NORM: "not", TAG: "RB"},
            {ORTH: "'ve", LEMMA: "have", NORM: "have", TAG: "VB"}]

        _exc[data[ORTH] + "ntve"] = [
            dict(data),
            {ORTH: "nt", LEMMA: "not", NORM: "not", TAG: "RB"},
            {ORTH: "ve", LEMMA: "have", NORM: "have", TAG: "VB"}]


for verb_data in [
    {ORTH: "could", NORM: "could", TAG: "MD"},
    {ORTH: "might", NORM: "might", TAG: "MD"},
    {ORTH: "must", NORM: "must", TAG: "MD"},
    {ORTH: "should", NORM: "should", TAG: "MD"},
    {ORTH: "would", NORM: "would", TAG: "MD"}]:
    verb_data_tc = dict(verb_data)
    verb_data_tc[ORTH] = verb_data_tc[ORTH].title()
    for data in [verb_data, verb_data_tc]:
        _exc[data[ORTH] + "'ve"] = [
            dict(data),
            {ORTH: "'ve", LEMMA: "have", TAG: "VB"}]

        _exc[data[ORTH] + "ve"] = [
            dict(data),
            {ORTH: "ve", LEMMA: "have", TAG: "VB"}]


for verb_data in [
    {ORTH: "ai", LEMMA: "be", TAG: "VBP", "number": 2},
    {ORTH: "are", LEMMA: "be", NORM: "are", TAG: "VBP", "number": 2},
    {ORTH: "is", LEMMA: "be", NORM: "is", TAG: "VBZ"},
    {ORTH: "was", LEMMA: "be", NORM: "was"},
    {ORTH: "were", LEMMA: "be", NORM: "were"},
    {ORTH: "have", NORM: "have"},
    {ORTH: "has", LEMMA: "have", NORM: "has"},
    {ORTH: "dare", NORM: "dare"}]:
    verb_data_tc = dict(verb_data)
    verb_data_tc[ORTH] = verb_data_tc[ORTH].title()
    for data in [verb_data, verb_data_tc]:
        _exc[data[ORTH] + "n't"] = [
            dict(data),
            {ORTH: "n't", LEMMA: "not", NORM: "not", TAG: "RB"}]

        _exc[data[ORTH] + "nt"] = [
            dict(data),
            {ORTH: "nt", LEMMA: "not", NORM: "not", TAG: "RB"}]


# Other contractions with trailing apostrophe

for exc_data in [
    {ORTH: "doin", LEMMA: "do", NORM: "doing"},
    {ORTH: "goin", LEMMA: "go", NORM: "going"},
    {ORTH: "nothin", LEMMA: "nothing", NORM: "nothing"},
    {ORTH: "nuthin", LEMMA: "nothing", NORM: "nothing"},
    {ORTH: "ol", LEMMA: "old", NORM: "old"},
    {ORTH: "somethin", LEMMA: "something", NORM: "something"}]:
    exc_data_tc = dict(exc_data)
    exc_data_tc[ORTH] = exc_data_tc[ORTH].title()
    for data in [exc_data, exc_data_tc]:
        data_apos = dict(data)
        data_apos[ORTH] = data_apos[ORTH] + "'"
        _exc[data[ORTH]] = [dict(data)]
        _exc[data_apos[ORTH]] = [dict(data_apos)]


# Other contractions with leading apostrophe

for exc_data in [
    {ORTH: "cause", LEMMA: "because", NORM: "because"},
    {ORTH: "em", LEMMA: PRON_LEMMA, NORM: "them"},
    {ORTH: "ll", LEMMA: "will", NORM: "will"},
    {ORTH: "nuff", LEMMA: "enough", NORM: "enough"}]:
    exc_data_apos = dict(exc_data)
    exc_data_apos[ORTH] = "'" + exc_data_apos[ORTH]
    for data in [exc_data, exc_data_apos]:
        _exc[data[ORTH]] = [data]


# Times

for h in range(1, 12 + 1):
    for period in ["a.m.", "am"]:
        _exc["%d%s" % (h, period)] = [
            {ORTH: "%d" % h},
            {ORTH: period, LEMMA: "a.m.", NORM: "a.m."}]
    for period in ["p.m.", "pm"]:
        _exc["%d%s" % (h, period)] = [
            {ORTH: "%d" % h},
            {ORTH: period, LEMMA: "p.m.", NORM: "p.m."}]


# Rest

_other_exc = {
    "y'all": [
        {ORTH: "y'", LEMMA: PRON_LEMMA, NORM: "you"},
        {ORTH: "all"}],

    "yall": [
        {ORTH: "y", LEMMA: PRON_LEMMA, NORM: "you"},
        {ORTH: "all"}],

    "how'd'y": [
        {ORTH: "how", LEMMA: "how"},
        {ORTH: "'d", LEMMA: "do"},
        {ORTH: "'y", LEMMA: PRON_LEMMA, NORM: "you"}],

    "How'd'y": [
        {ORTH: "How", LEMMA: "how", NORM: "how"},
        {ORTH: "'d", LEMMA: "do"},
        {ORTH: "'y", LEMMA: PRON_LEMMA, NORM: "you"}],

    "not've": [
        {ORTH: "not", LEMMA: "not", TAG: "RB"},
        {ORTH: "'ve", LEMMA: "have", NORM: "have", TAG: "VB"}],

    "notve": [
        {ORTH: "not", LEMMA: "not", TAG: "RB"},
        {ORTH: "ve", LEMMA: "have", NORM: "have", TAG: "VB"}],

    "Not've": [
        {ORTH: "Not", LEMMA: "not", NORM: "not", TAG: "RB"},
        {ORTH: "'ve", LEMMA: "have", NORM: "have", TAG: "VB"}],

    "Notve": [
        {ORTH: "Not", LEMMA: "not", NORM: "not", TAG: "RB"},
        {ORTH: "ve", LEMMA: "have", NORM: "have", TAG: "VB"}],

    "cannot": [
        {ORTH: "can", LEMMA: "can", TAG: "MD"},
        {ORTH: "not", LEMMA: "not", TAG: "RB"}],

    "Cannot": [
        {ORTH: "Can", LEMMA: "can", NORM: "can", TAG: "MD"},
        {ORTH: "not", LEMMA: "not", TAG: "RB"}],

    "gonna": [
        {ORTH: "gon", LEMMA: "go", NORM: "going"},
        {ORTH: "na", LEMMA: "to", NORM: "to"}],

    "Gonna": [
        {ORTH: "Gon", LEMMA: "go", NORM: "going"},
        {ORTH: "na", LEMMA: "to", NORM: "to"}],

    "gotta": [
        {ORTH: "got"},
        {ORTH: "ta", LEMMA: "to", NORM: "to"}],

    "Gotta": [
        {ORTH: "Got", NORM: "got"},
        {ORTH: "ta", LEMMA: "to", NORM: "to"}],

    "let's": [
        {ORTH: "let"},
        {ORTH: "'s", LEMMA: PRON_LEMMA, NORM: "us"}],

    "Let's": [
        {ORTH: "Let", LEMMA: "let", NORM: "let"},
        {ORTH: "'s", LEMMA: PRON_LEMMA, NORM: "us"}]
}

_exc.update(_other_exc)


for exc_data in [
    {ORTH: "'S", LEMMA: "'s", NORM: "'s"},
    {ORTH: "'s", LEMMA: "'s", NORM: "'s"},
    {ORTH: "\u2018S", LEMMA: "'s", NORM: "'s"},
    {ORTH: "\u2018s", LEMMA: "'s", NORM: "'s"},
    {ORTH: "and/or", LEMMA: "and/or", NORM: "and/or", TAG: "CC"},
    {ORTH: "w/o", LEMMA: "without", NORM: "without"},
    {ORTH: "'re", LEMMA: "be", NORM: "are"},
    {ORTH: "'Cause", LEMMA: "because", NORM: "because"},
    {ORTH: "'cause", LEMMA: "because", NORM: "because"},
    {ORTH: "'cos", LEMMA: "because", NORM: "because"},
    {ORTH: "'Cos", LEMMA: "because", NORM: "because"},
    {ORTH: "'coz", LEMMA: "because", NORM: "because"},
    {ORTH: "'Coz", LEMMA: "because", NORM: "because"},
    {ORTH: "'cuz", LEMMA: "because", NORM: "because"},
    {ORTH: "'Cuz", LEMMA: "because", NORM: "because"},
    {ORTH: "'bout", LEMMA: "about", NORM: "about"},
    {ORTH: "ma'am", LEMMA: "madam", NORM: "madam"},
    {ORTH: "Ma'am", LEMMA: "madam", NORM: "madam"},
    {ORTH: "o'clock", LEMMA: "o'clock", NORM: "o'clock"},
    {ORTH: "O'clock", LEMMA: "o'clock", NORM: "o'clock"},
    {ORTH: "lovin'", LEMMA: "love", NORM: "loving"},
    {ORTH: "Lovin'", LEMMA: "love", NORM: "loving"},
    {ORTH: "lovin", LEMMA: "love", NORM: "loving"},
    {ORTH: "Lovin", LEMMA: "love", NORM: "loving"},
    {ORTH: "havin'", LEMMA: "have", NORM: "having"},
    {ORTH: "Havin'", LEMMA: "have", NORM: "having"},
    {ORTH: "havin", LEMMA: "have", NORM: "having"},
    {ORTH: "Havin", LEMMA: "have", NORM: "having"},
    {ORTH: "doin'", LEMMA: "do", NORM: "doing"},
    {ORTH: "Doin'", LEMMA: "do", NORM: "doing"},
    {ORTH: "doin", LEMMA: "do", NORM: "doing"},
    {ORTH: "Doin", LEMMA: "do", NORM: "doing"},
    {ORTH: "goin'", LEMMA: "go", NORM: "going"},
    {ORTH: "Goin'", LEMMA: "go", NORM: "going"},
    {ORTH: "goin", LEMMA: "go", NORM: "going"},
    {ORTH: "Goin", LEMMA: "go", NORM: "going"},


    {ORTH: "Mt.", LEMMA: "Mount", NORM: "Mount"},
    {ORTH: "Ak.", LEMMA: "Alaska", NORM: "Alaska"},
    {ORTH: "Ala.", LEMMA: "Alabama", NORM: "Alabama"},
    {ORTH: "Apr.", LEMMA: "April", NORM: "April"},
    {ORTH: "Ariz.", LEMMA: "Arizona", NORM: "Arizona"},
    {ORTH: "Ark.", LEMMA: "Arkansas", NORM: "Arkansas"},
    {ORTH: "Aug.", LEMMA: "August", NORM: "August"},
    {ORTH: "Calif.", LEMMA: "California", NORM: "California"},
    {ORTH: "Colo.", LEMMA: "Colorado", NORM: "Colorado"},
    {ORTH: "Conn.", LEMMA: "Connecticut", NORM: "Connecticut"},
    {ORTH: "Dec.", LEMMA: "December", NORM: "December"},
    {ORTH: "Del.", LEMMA: "Delaware", NORM: "Delaware"},
    {ORTH: "Feb.", LEMMA: "February", NORM: "February"},
    {ORTH: "Fla.", LEMMA: "Florida", NORM: "Florida"},
    {ORTH: "Ga.", LEMMA: "Georgia", NORM: "Georgia"},
    {ORTH: "Ia.", LEMMA: "Iowa", NORM: "Iowa"},
    {ORTH: "Id.", LEMMA: "Idaho", NORM: "Idaho"},
    {ORTH: "Ill.", LEMMA: "Illinois", NORM: "Illinois"},
    {ORTH: "Ind.", LEMMA: "Indiana", NORM: "Indiana"},
    {ORTH: "Jan.", LEMMA: "January", NORM: "January"},
    {ORTH: "Jul.", LEMMA: "July", NORM: "July"},
    {ORTH: "Jun.", LEMMA: "June", NORM: "June"},
    {ORTH: "Kan.", LEMMA: "Kansas", NORM: "Kansas"},
    {ORTH: "Kans.", LEMMA: "Kansas", NORM: "Kansas"},
    {ORTH: "Ky.", LEMMA: "Kentucky", NORM: "Kentucky"},
    {ORTH: "La.", LEMMA: "Louisiana", NORM: "Louisiana"},
    {ORTH: "Mar.", LEMMA: "March", NORM: "March"},
    {ORTH: "Mass.", LEMMA: "Massachusetts", NORM: "Massachusetts"},
    {ORTH: "May.", LEMMA: "May", NORM: "May"},
    {ORTH: "Mich.", LEMMA: "Michigan", NORM: "Michigan"},
    {ORTH: "Minn.", LEMMA: "Minnesota", NORM: "Minnesota"},
    {ORTH: "Miss.", LEMMA: "Mississippi", NORM: "Mississippi"},
    {ORTH: "N.C.", LEMMA: "North Carolina", NORM: "North Carolina"},
    {ORTH: "N.D.", LEMMA: "North Dakota", NORM: "North Dakota"},
    {ORTH: "N.H.", LEMMA: "New Hampshire", NORM: "New Hampshire"},
    {ORTH: "N.J.", LEMMA: "New Jersey", NORM: "New Jersey"},
    {ORTH: "N.M.", LEMMA: "New Mexico", NORM: "New Mexico"},
    {ORTH: "N.Y.", LEMMA: "New York", NORM: "New York"},
    {ORTH: "Neb.", LEMMA: "Nebraska", NORM: "Nebraska"},
    {ORTH: "Nebr.", LEMMA: "Nebraska", NORM: "Nebraska"},
    {ORTH: "Nev.", LEMMA: "Nevada", NORM: "Nevada"},
    {ORTH: "Nov.", LEMMA: "November", NORM: "November"},
    {ORTH: "Oct.", LEMMA: "October", NORM: "October"},
    {ORTH: "Okla.", LEMMA: "Oklahoma", NORM: "Oklahoma"},
    {ORTH: "Ore.", LEMMA: "Oregon", NORM: "Oregon"},
    {ORTH: "Pa.", LEMMA: "Pennsylvania", NORM: "Pennsylvania"},
    {ORTH: "S.C.", LEMMA: "South Carolina", NORM: "South Carolina"},
    {ORTH: "Sep.", LEMMA: "September", NORM: "September"},
    {ORTH: "Sept.", LEMMA: "September", NORM: "September"},
    {ORTH: "Tenn.", LEMMA: "Tennessee", NORM: "Tennessee"},
    {ORTH: "Va.", LEMMA: "Virginia", NORM: "Virginia"},
    {ORTH: "Wash.", LEMMA: "Washington", NORM: "Washington"},
    {ORTH: "Wis.", LEMMA: "Wisconsin", NORM: "Wisconsin"}]:
    _exc[exc_data[ORTH]] = [exc_data]


extra_abbrs = ['abbrev.', 'Abbrev.', 'Abd.', 'Aberd.', 'Aberdeensh.', 'abl.', 'Abol.', 'Aborig.', 'Abp.', 'Abr.', 'Abridg.', 'Abridgem.', 'absol.', 'Absol.', 'Abst.', 'abstr.', 'Abstr.', 'Acad.', 'acc.', 'Acc.', 'Accomm.', 'Accompl.', 'Accs.', 'Acct.', 'Accts.', 'accus.', 'Achievem.', 'Add.', 'Addit.', 'Addr.', 'adj.', 'adjs.', 'Adm.', 'Admir.', 'Admon.', 'Admonit.', 'adv.', 'Adv.', 'Advancem.', 'advb.', 'Advert.', 'Advoc.', 'advs.', 'Advt.', 'Advts.', 'Aerodynam.', 'Aeronaut.', 'Aff.', 'Afr.', 'Agric.', 'agst.', 'al.', 'Alch.', 'Alg.', 'Alleg.', 'Allit.', 'Alm.', 'Alph.', 'alt.', 'Amer.', 'Analyt.', 'Anat.', 'Anc.', 'Anecd.', 'Ang.', 'Angl.', 'Anglo-Ind.', 'Anim.', 'Ann.', 'Anniv.', 'Annot.', 'Anon.', 'Answ.', 'Anthrop.', 'Anthropol.', 'Antiq.', 'aphet.', 'Apoc.', 'Apol.', 'Appl.', 'Applic.', 'appos.', 'Arb.', 'Archaeol.', 'Archit.', 'Argt.', 'Arith.', 'Arithm.', 'Arrangem.', 'arrv.', 'Artic.', 'Artific.', 'Artill.', 'Ashm.', 'Assemb.', 'Assoc.', 'Assyriol.', 'Astr.', 'Astrol.', 'Astron.', 'Att.', 'attrib.', 'Attrib.', 'Austral.', 'Auth.', 'Autobiog.', 'Autobiogr.', 'Ave.', 'Ayrsh.', 'Bacteriol.', 'Bedfordsh.', 'bef.', 'Belg.', 'Berks.', 'Berksh.', 'Berw.', 'Berwicksh.', 'betw.', 'Bibliogr.', 'Biochem.', 'Biog.', 'Biogr.', 'Biol.', 'Bk.', 'Bks.', 'Blvd.', 'Bord.', 'Bp.', 'Braz.', 'Bros.', 'Bur.', 'Cal.', 'Calc.', 'Calend.', 'Calif.', 'Calligr.', 'Camb.', 'Cambr.', 'Campanol.', 'Canad.', 'Canterb.', 'Capt.', 'Cartogr.', 'Catal.', 'Catech.', 'Cath.', 'Ceram.',
    'Cert.',
    'Certif.',
    'cf.',
    'Ch.',
    'Chamb.',
    'Char.',
    'Charac.',
    'Chas.',
    'Chem.',
    'Chesh.',
    'Chr.',
    'Chron.',
    'Chronol.',
    'Chrons.',
    'Cinematogr.',
    'Circ.',
    'cl.',
    'Cl.',
    'Classif.',
    'Climatol.',
    'Clin.',
    'Co.',
    'Col.',
    'Coll.',
    'colloq.',
    'Colloq.',
    'Com.',
    'Comm.',
    'Commandm.',
    'Commend.',
    'Commerc.',
    'Commiss.',
    'Commonw.',
    'Communic.',
    'comp.',
    'Comp.',
    'Compan.',
    'compar.',
    'Compar.',
    'Compend.',
    'compl.',
    'Compl.',
    'Compos.',
    'conc.',
    'Conc.',
    'Conch.',
    'Concl.',
    'concr.',
    'Conf.',
    'Confid.',
    'Confl.',
    'Confut.',
    'Congr.',
    'Congreg.',
    'conj.',
    'Conn.',
    'cons.',
    'Consc.',
    'Consecr.',
    'Consid.',
    'Consol.',
    'const.',
    'Constit.',
    'Constr.',
    'Contemp.',
    'Contempl.',
    'contempt.',
    'Contend.',
    'Contin.',
    'contr.',
    'Contrib.',
    'Controv.',
    'Conv.',
    'Conversat.',
    'Convoc.',
    'Cor.',
    'Cornw.',
    'Coron.',
    'Corp.',
    'Corr.',
    'corresp.',
    'Corresp.',
    'Counc.',
    'Courtsh.',
    'cpd.',
    'Craniol.',
    'Craniom.',
    'Crim.',
    'Crit.',
    'Crt.',
    'Crts.',
    'Cryptogr.',
    'Crystallogr.',
    'Ct.',
    'Cumb.',
    'Cumberld.',
    'Cumbld.',
    'Cycl.',
    'Cytol.',
    'dat.',
    'Dau.',
    'Deb.',
    'Declar.',
    'Ded.',
    'def.',
    'Def.',
    'Deliv.',
    'dem.',
    'Demonstr.',
    'Dep.',
    'Depred.',
    'Depredat.',
    'Dept.',
    'Derbysh.',
    'deriv.',
    'derog.',
    'Descr.',
    'Deut.',
    'Devel.',
    'Devonsh.',
    'Dict.',
    'Diffic.',
    'dim.',
    'Dis.',
    'Discipl.',
    'Discov.',
    'Discrim.',
    'Diss.',
    'Dist.',
    'Distemp.',
    'Distill.',
    'Distrib.',
    'Div.',
    'Divers.',
    'Dk.',
    'Doc.',
    'Doct.',
    'Domest.',
    'Dr.',
    'Drs.',
    'Durh.',
    'dyslog.',
    'Eccl.',
    'Eccles.',
    'Ecclus.',
    'Ecol.',
    'Econ.',
    'ed.',
    'Ed.',
    'Edin.',
    'Edinb.',
    'Educ.',
    'Edw.',
    'Egypt.',
    'Egyptol.',
    'Electr.',
    'Electro-magn.',
    'Electro-physiol.',
    'Elem.',
    'Eliz.',
    'Elizab.',
    'ellipt.',
    'Emb.',
    'Embryol.',
    'emph.',
    'encl.',
    'Encycl.',
    'Eng.',
    'Engin.',
    'Englishw.',
    'Enq.',
    'Ent.',
    'Enthus.',
    'Entom.',
    'Entomol.',
    'Enzymol.',
    'Ep.',
    'Eph.',
    'Ephes.',
    'Epil.',
    'Episc.',
    'Epist.',
    'Epit.',
    'Equip.',
    'erron.',
    'Esd.',
    'esp.',
    'Ess.',
    'Essent.',
    'Establ.',
    'Esth.',
    'etc.',
    'Ethnol.',
    'etym.',
    'etymol.',
    'Etymol.',
    'euphem.',
    'Eval.',
    'Evang.',
    'Evid.',
    'Evol.',
    'Exalt.',
    'exc.',
    'Exch.',
    'Exec.',
    'Exerc.',
    'Exhib.',
    'Exod.',
    'Exped.',
    'Exper.',
    'Explan.',
    'Explic.',
    'Explor.',
    'Expos.',
    'ext.',
    'Ezek.',
    'Fab.',
    'fam.',
    'Fam.',
    'famil.',
    'Farew.',
    'fem.',
    'Ff.',
    'Fifesh.',
    'fig.',
    'fl.',
    'Footpr.',
    'Forfarsh.',
    'Fortif.',
    'Fortn.',
    'Found.',
    'Fr.',
    'Fragm.',
    'Fratern.',
    'freq.',
    'Friendsh.',
    'ft.',
    'Furnit.',
    'fut.',
    'Gal.',
    'Gard.',
    'Gastron.',
    'Gaz.',
    'Gd.',
    'gen.',
    'Gen.',
    'Geo.',
    'Geog.',
    'Geogr.',
    'Geol.',
    'Geom.',
    'Geomorphol.',
    'Ger.',
    'Glac.',
    'Glasg.',
    'Glos.',
    'Gloss.',
    'Glouc.',
    'Gloucestersh.',
    'Gosp.',
    'Gov.',
    'Govt.',
    'Gr.',
    'Gram.',
    'Gt.',
    'Gynaecol.',
    'Hab.',
    'Haematol.',
    'Hag.',
    'Hampsh.',
    'Handbk.',
    'Hants.',
    'Heb.',
    'Hebr.',
    'Hen.',
    'Herb.',
    'Heref.',
    'Herefordsh.',
    'Hertfordsh.',
    'Hierogl.',
    'hist.',
    'Hist.',
    'Histol.',
    'Hom.',
    'Horol.',
    'Hort.',
    'Hos.',
    'Hosp.',
    'Househ.',
    'Housek.',
    'Husb.',
    'Hydraul.',
    'Hydrol.',
    'Ichth.',
    'Icthyol.',
    'Ideol.',
    'Idol.',
    'Illustr.',
    'Imag.',
    'imit.',
    'Immunol.',
    'imp.',
    'imperf.',
    'impers.',
    'impf.',
    'Impr.',
    'improp.',
    'Inaug.',
    'Inc.',
    'Inclos.',
    'ind.',
    'Ind.',
    'indef.',
    'indic.',
    'indir.',
    'Industr.',
    'infin.',
    'infl.',
    'Infl.',
    'Innoc.',
    'Inorg.',
    'Inq.',
    'Inst.',
    'instr.',
    'Instr.',
    'int.',
    'Intell.',
    'Interc.',
    'interj.',
    'Interl.',
    'Internat.',
    'Interpr.',
    'interrog.',
    'intr.',
    'intrans.',
    'Intro.',
    'Introd.',
    'Inv.',
    'Invertebr.',
    'Investig.',
    'Investm.',
    'Invoc.',
    'Ir.',
    'Irel.',
    'iron.',
    'irreg.',
    'Isa.',
    'Ital.',
    'Jahrb.',
    'Jam.',
    'Jap.',
    'Jas.',
    'Jer.',
    'joc.',
    'Josh.',
    'Jr.',
    'Jrnl.',
    'Jrnls.',
    'Jud.',
    'Judg.',
    'Jurisd.',
    'Jurisdict.',
    'Jurispr.',
    'Justif.',
    'Justific.',
    'Kgs.',
    'Kingd.',
    'Knowl.',
    'Kpr.',
    'Lam.',
    'Lanc.',
    'Lancash.',
    'Lancs.',
    'Lang.',
    'Langs.',
    'Lat.',
    'lb.',
    'Ld.',
    'Lds.',
    'Lect.',
    'Leechd.',
    'Leicest.',
    'Leicestersh.',
    'Leics.',
    'Let.',
    'Lett.',
    'Lev.',
    'Lex.',
    'Libr.',
    'Limnol.',
    'Lincolnsh.',
    'Lincs.',
    'Ling.',
    'Linn.',
    'lit.',
    'Lit.',
    'Lithogr.',
    'Lithol.',
    'Liturg.',
    'll.',
    'Lond.',
    'Lt.',
    'Ltd.',
    'Macc.',
    'Mach.',
    'Mag.',
    'Magn.',
    'Mal.',
    'Managem.',
    'Manch.',
    'Manip.',
    'Manuf.',
    'masc.',
    'Matt.',
    'Meas.',
    'Measurem.',
    'Mech.',
    'med.',
    'Med.',
    'Medit.',
    'Mem.',
    'Merc.',
    'Merch.',
    'Metall.',
    'Metallif.',
    'Metallogr.',
    'Metamorph.',
    'Metaph.',
    'metaphor.',
    'Meteorol.',
    'Metrop.',
    'Mex.',
    'Mic.',
    'Mich.',
    'Microbiol.',
    'Microsc.',
    'midl.',
    'Mil.',
    'Milit.',
    'Min.',
    'Mineral.',
    'Misc.',
    'Miscell.',
    'mispr.',
    'Monum.',
    'Morphol.',
    'Mr.',
    'Mrs.',
    'MS.',
    'M.Sc.',
    'MSS.',
    'Mt.',
    'Mtg.',
    'Mts.',
    'Munic.',
    'Munif.',
    'Munim.',
    'Mus.',
    'Myst.',
    'Mythol.',
    'Nah.',
    'Narr.',
    'Narrat.',
    'Nat.',
    'Naut.',
    'Nav.',
    'Navig.',
    'Neh.',
    'Neighb.',
    'Nerv.',
    'Neurol.',
    'Neurosurg.',
    'Newc.',
    'Newspr.',
    'nom.',
    'nonce-wd.',
    'Non-conf.',
    'Nonconf.',
    'Norf.',
    'Northamptonsh.',
    'Northants.',
    'Northumb.',
    'Northumbld.',
    'Northumbr.',
    'Norw.',
    'Norweg.',
    'Notts.',
    'ns.',
    'Nucl.',
    'Num.',
    'Numism.',
    'Obad.',
    'Obed.',
    'obj.',
    'Obj.',
    'obl.',
    'obs.',
    'Obs.',
    'Observ.',
    'Obstet.',
    'Obstetr.',
    'occas.',
    'Occas.',
    'Occup.',
    'Occurr.',
    'Oceanogr.',
    'Offic.',
    'Okla.',
    'Ont.',
    'Ophthalm.',
    'Ophthalmol.',
    'opp.',
    'Oppress.',
    'Opt.',
    'Orac.',
    'Ord.',
    'Org.',
    'orig.',
    'Orig.',
    'Orkn.',
    'Ornith.',
    'Ornithol.',
    'Orthogr.',
    'Outl.',
    'Oxf.',
    'Oxfordsh.',
    'Oxon.',
    'oz.',
    'pa.',
    'Pa.',
    'Palaeobot.',
    'Palaeogr.',
    'Palaeont.',
    'Palaeontol.',
    'Paraphr.',
    'Parasitol.',
    'Parl.',
    'Parnass.',
    'Pathol.',
    'Peculat.',
    'Penins.',
    'perf.',
    'Perf.',
    'perh.',
    'Periodontol.',
    'pers.',
    'Pers.',
    'Persec.',
    'personif.',
    'Perthsh.',
    'Petrogr.',
    'pf.',
    'Pharm.',
    'Pharmaceut.',
    'Pharmacol.',
    'Ph.D.',
    'Phil.',
    'Philad.',
    'Philem.',
    'Philipp.',
    'Philol.',
    'Philos.',
    'Phoen.',
    'phonet.',
    'Phonol.',
    'Photog.',
    'Photogr.',
    'phr.',
    'Phrenol.',
    'Phys.',
    'Physiogr.',
    'Physiol.',
    'Pict.',
    'pl.',
    'plur.',
    'Pol.',
    'Polit.',
    'Polytechn.',
    'Porc.',
    'poss.',
    'Posth.',
    'Postm.',
    'ppl.',
    'pple.',
    'pples.',
    'Pract.',
    'prec.',
    'pred.',
    'predic.',
    'Predict.',
    'pref.',
    'Pref.',
    'Preh.',
    'Prehist.',
    'prep.',
    'Prerog.',
    'pres.',
    'Pres.',
    'Presb.',
    'Preserv.',
    'Prim.',
    'Princ.',
    'priv.',
    'prob.',
    'Probab.',
    'Probl.',
    'Proc.',
    'Prod.',
    'Prof.',
    'Prol.',
    'pron.',
    'pronunc.',
    'Pronunc.',
    'prop.',
    'Prop.',
    'propr.',
    'Pros.',
    'prov.',
    'Prov.',
    'Provid.',
    'Provinc.',
    'Provis.',
    'Ps.',
    'pseudo-arch.',
    'pseudo-dial.',
    'pseudo-Sc.',
    'Psych.',
    'Psychoanal.',
    'Psychoanalyt.',
    'Psychol.',
    'Psychopathol.',
    'Pt.',
    'Publ.',
    'Purg.',
    'Qld.',
    'quot.',
    'quots.',
    'Radiol.',
    'Reas.',
    'Reb.',
    'Rec.',
    'Reclam.',
    'Recoll.',
    'Redempt.',
    'redupl.',
    'Ref.',
    'refash.',
    'refl.',
    'Refl.',
    'Refus.',
    'Refut.',
    'reg.',
    'Reg.',
    'Regic.',
    'Regist.',
    'Regr.',
    'rel.',
    'Rel.',
    'Relig.',
    'Reminisc.',
    'Remonstr.',
    'Renfrewsh.',
    'Rep.',
    'repr.',
    'Reprod.',
    'Reps.',
    'Rept.',
    'Repub.',
    'Res.',
    'Resid.',
    'Ret.',
    'Retrosp.',
    'Rev.',
    'Revol.',
    'rhet.',
    'Rhet.',
    'Rich.',
    'Ross-sh.',
    'Roxb.',
    'Roy.',
    'Rudim.',
    'Russ.',
    'Sam.',
    'Sask.',
    'Sat.',
    'sc.',
    'Sc.',
    'Scand.',
    'Sch.',
    'Sci.',
    'Scot.',
    'Scotl.',
    'Script.',
    'Sculpt.',
    'Seismol.',
    'Sel.',
    'Sen.',
    'Ser.',
    'Serm.',
    'Sess.',
    'Settlem.',
    'Sev.',
    'Shakes.',
    'Shaks.',
    'Sheph.',
    'Shetl.',
    'Shropsh.',
    'Soc.',
    'Sociol.',
    'Som.',
    'Sonn.',
    'sp.',
    'spec.',
    'Spec.',
    'Specif.',
    'Specim.',
    'Spectrosc.',
    'Sq.',
    'Sr.',
    'SS.',
    'St.',
    'Staffordsh.',
    'Staffs.',
    'Stat.',
    'Statist.',
    'Ste.',
    'str.',
    'Stratigr.',
    'Struct.',
    'Sts.',
    'Stud.',
    'subj.',
    'Subj.',
    'subjunct.',
    'subord.',
    'Subscr.',
    'Subscript.',
    'subseq.',
    'subst.',
    'suff.',
    'Suff.',
    'superl.',
    'Suppl.',
    'Supplic.',
    'Suppress.',
    'Surg.',
    'Surv.',
    'Sus.',
    'syll.',
    'Symmetr.',
    'Symp.',
    'Syst.',
    'Taxon.',
    'techn.',
    'Techn.',
    'Technol.',
    'Tel.',
    'Telecomm.',
    'Telegr.',
    'Teleph.',
    'Teratol.',
    'Terminol.',
    'Terrestr.',
    'Textbk.',
    'Theat.',
    'Theatr.',
    'Theol.',
    'Theoret.',
    'Thermonucl.',
    'Thes.',
    'Thess.',
    'Topogr.',
    'tr.',
    'Trad.',
    'Trag.',
    'trans.',
    'Trans.',
    'transf.',
    'transl.',
    'Transl.',
    'Transubstant.',
    'Trav.',
    'Treas.',
    'Treatm.',
    'Trib.',
    'Trig.',
    'Trigonom.',
    'Trop.',
    'Troub.',
    'Troubl.',
    'Typog.',
    'Typogr.',
    'ult.',
    'Univ.',
    'unkn.',
    'Unnat.',
    'Unoffic.',
    'unstr.',
    'usu.',
    'Utilit.',
    'Va.',
    'Vac.',
    'Valedict.',
    'var.',
    'varr.',
    'vars.',
    'vb.',
    'vbl.',
    'vbs.',
    'Veg.',
    'Venet.',
    'Vertebr.',
    'Vet.',
    'Vic.',
    'Vict.',
    'Vind.',
    'Vindic.',
    'Virg.',
    'Virol.',
    'viz.',
    'Voc.',
    'Vocab.',
    'Vol.',
    'Vols.',
    'Voy.',
    'vs.',
    'vulg.',
    'Vulg.',
    'Warwicksh.',
    'wd.',
    'Wd.',
    'Westm.',
    'Westmld.',
    'Westmorld.',
    'Westmrld.',
    'Wilts.',
    'Wiltsh.',
    'Wis.',
    'Wisd.',
    'wk.',
    'Wk.',
    'Wkly.',
    'Wks.',
    'Wonderf.',
    'Worc.',
    'Worcestersh.',
    'Worcs.',
    'Writ.',
    'Yearbk.',
    'Yng.',
    'Yorks.',
    'Yorksh.',
    'Yr.',
    'Yrs.',
    'Zech.',
    'Zeitschr.',
    'Zeph.',
    'Zoogeogr.',
    'Zool.'
]


for orth in [
    "'d", "a.m.", "Adm.", "Bros.", "co.", "Co.", "Corp.", "D.C.", "Dr.", "e.g.",
    "E.g.", "E.G.", "Gen.", "Gov.", "i.e.", "I.e.", "I.E.", "Inc.", "Jr.",
    "Ltd.", "Md.", "Messrs.", "Mo.", "Mont.", "Mr.", "Mrs.", "Ms.", "p.m.",
    "Ph.D.", "Rep.", "Rev.", "Sen.", "St.", "vs."]:
    _exc[orth] = [{ORTH: orth}]

for orth in extra_abbrs:
    _exc[orth] = [{ORTH: orth}]


for string in _exclude:
    if string in _exc:
        _exc.pop(string)


TOKENIZER_EXCEPTIONS = _exc
