from __future__ import division

documentText = "The University of California, Riverside is one of 10 universities within the prestigious University of California system, and the only UC located in Inland Southern California. Widely recognized as one of the most ethnically diverse research universities in the nation."

doc = documentText.lower()
doc = doc.replace('universities','university').split(" ")

wc_university = doc.count("university")
wc_riverside = doc.count("riverside")
wc_diverse = doc.count("diverse")

print(wc_university)
len_doc = len(doc)

query1UNI = (wc_university/len_doc)* \
            (wc_riverside/len_doc)
query2UNI = (wc_diverse/len_doc)* \
            (wc_university/len_doc)

print('**************************************************')
print('******Before  smoothing method******')
print('UM Score for q1 is %.4f' % round(query1UNI,6))
print('UM Score for q2 is %.4f' % round(query2UNI,6))

def laplace_smoothing(count, len_doc, k):
    return (count+k)/(len_doc+(count*k))

k = 1
query1UNI = laplace_smoothing(wc_university, len_doc, k)* \
            laplace_smoothing(wc_riverside, len_doc, k)
query2UNI = laplace_smoothing(wc_diverse, len_doc, k)* \
            laplace_smoothing(wc_riverside, len_doc, k)

print('******After laplace smoothing method******')
print('UM Score for q1 is %.4f' % round(query1UNI,6))
print('UM Score for q2 is %.4f' % round(query2UNI,6))
print('**************************************************')
