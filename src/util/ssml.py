# Speech Synthesis Markup Language (SSML) helpers
import re

def split_sentences(st):
    sentences = re.split(r'[.?!]\s*', st)
    if sentences[-1]:
        return sentences
    else:
        return sentences[:-1]

def insert_sentence_breaks(message, time_milliseconds):
    body = ""
    sentences = split_sentences(message)
    for sentence in sentences:
        body = f'''
            {body}
            {sentence}
            <break  time="{time_milliseconds}"/>
        '''
    return body

def build_ssml(message, voice, style):
    # body = insert_sentence_breaks(message=message, time_milliseconds=10)
    return f'''
    <speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xmlns:mstts="https://www.w3.org/2001/mstts" xml:lang="en-US">
        <voice name="{voice}" styledegree="2">
            <break  time="200"/>
            <mstts:silence  type="Sentenceboundary" value="35ms"/>
            <mstts:express-as style="{style}">
                {message}
            </mstts:express-as>
             <break  time="50"/>
        </voice>
    </speak>
    '''
    # return f'''
    # <speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xmlns:mstts="https://www.w3.org/2001/mstts" xml:lang="en-US">
    #     <voice name="{voice}">{message}</voice>
    # </speak>
    # '''