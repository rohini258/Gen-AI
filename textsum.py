import nltk
import string
from heapq import nlargest


nltk.download('punkt_tab')
nltk.download('stopwords')

text="""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. Sed nisi. Nulla quis sem at nibh elementum imperdiet. Duis sagittis ipsum. Praesent mauris. Fusce nec tellus sed augue semper porta. Mauris massa. Vestibulum lacinia arcu eget nulla. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Curabitur sodales ligula in libero. Sed dignissim lacinia nunc. Curabitur tortor. Pellentesque nibh. Aenean quam. In scelerisque sem at dolor. Maecenas mattis. Sed convallis tristique sem. Proin ut ligula vel nunc egestas porttitor. Morbi lectus risus, iaculis vel, suscipit quis, iaculis ut, libero. Aenean et tellus in sapien placerat adipiscing Phasellus a est. Mauris vitae leo. Donec justo. Nam ipsum. Cras vitae turpis vel ipsum rutrum pharetra. Integer a nibh. In egestas. Donec non mi. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt.
This text is a standard Lorem Ipsum passage and is intended solely as a placeholder. 
The length may vary slightly depending on display settings. Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor.
Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. 
Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. 
Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. 
Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque sed ipsum. Nam quam nunc, blandit vel, luctus pulvinar, hendrerit id, lorem. Maecenas nec odio et ante tincidunt tempus. Donec vitae sapien ut libero venenatis faucibus. Nullam quis ante. Etiam sit amet orci eget eros faucibus tincidunt. Duis leo. Sed fringilla mauris sit amet nibh. Donec sodales sagittis magna. 
Sed consequat, leo eget bibendum sodales, augue velit cursus nunc."""
 
if text.count(".")<20:
    length=int(round(text.count(".")/15,0))
else:
    length=1

nopuch="".join([char for char in text if char not in string.punctuation])

stopwords=nltk.corpus.stopwords.words('english')
processed_text=[word for word in nopuch.split() if word.lower() not in stopwords]

word_freq={}
for word in processed_text:
    word_freq[word]=word_freq.get(word,0)+1

max_freq=max(word_freq.values())
for word in word_freq.keys():
    word_freq[word]=word_freq[word]/max_freq 

sent_list=nltk.sent_tokenize(text)
sent_score={}
for sent in sent_list:
    for word in nltk.word_tokenize(sent.lower()):
        if word in word_freq:
            sent_score[sent]=sent_score.get(sent,0)+word_freq[word]

summary_sents=nlargest(length,sent_score,key=sent_score.get)
summary=".".join(summary_sents)
print("summary:\n",summary)






    

