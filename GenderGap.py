import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
% matplotlib inline
women_degrees=pd.read_csv("percent-bachelors-degrees-women-usa.csv")
major_cat=['Computer Science','Physical Sciences','Agriculture', 'Architecture']
fig=plt.figure(figsize=(12,4))
for i in range(0,4):
    ax=fig.add_subplot(1,4,i+1)
    ax.plot(women_degrees['Year'],women_degrees[major_cat[i]],c='g',label='women',linewidth=2)
    ax.plot(women_degrees['Year'],100-women_degrees[major_cat[i]],c='r',label='men',linewidth=2)
    for key,spine in ax.spines.items():
        spine.set_visible(False)
    ax.set_xlim(1968,2011)
    ax.set_ylim(0,85)
    ax.set_title(major_cat[i]) 
    ax.tick_params(bottom='off',top='off',right='off',left='off')
    #ax.text(1970,12,'men')
    #ax.text(1970,75,'women')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()
major_cat=['Business','Math and Statistics','Social Sciences and History', 'Biology']
fig=plt.figure(figsize=(12,4))
for i in range(0,4):
    ax=fig.add_subplot(1,4,i+1)
    ax.plot(women_degrees['Year'],women_degrees[major_cat[i]],c='g',label='women',linewidth=2)
    ax.plot(women_degrees['Year'],100-women_degrees[major_cat[i]],c='r',label='men',linewidth=2)
    for key,spine in ax.spines.items():
        spine.set_visible(False)
    ax.set_xlim(1968,2011)
    ax.set_ylim(0,85)
    ax.set_title(major_cat[i])
    ax.tick_params(bottom='off',top='off',right='off',left='off')
    #ax.text(1970,12,'men')
    #ax.text(1970,75,'women')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()
major_cat=['Communications and Journalism','Art and Performance','English','Psychology']
fig=plt.figure(figsize=(12,4))
for i in range(0,4):
    ax=fig.add_subplot(1,4,i+1)
    ax.plot(women_degrees['Year'],women_degrees[major_cat[i]],c='g',label='women',linewidth=2)
    ax.plot(women_degrees['Year'],100-women_degrees[major_cat[i]],c='r',label='men',linewidth=2)
    for key,spine in ax.spines.items():
        spine.set_visible(False)
    ax.set_xlim(1968,2011)
    ax.set_ylim(0,85)
    ax.set_title(major_cat[i])
    ax.tick_params(bottom='off',top='off',right='off',left='off')
    #ax.text(1970,12,'men')
    #ax.text(1970,75,'women')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()
major_cat=['Foreign Languages','Public Administration','Education','Health Professions']
fig=plt.figure(figsize=(12,4))
for i in range(0,4):
    ax=fig.add_subplot(1,4,i+1)
    ax.plot(women_degrees['Year'],women_degrees[major_cat[i]],c='g',label='women',linewidth=2)
    ax.plot(women_degrees['Year'],100-women_degrees[major_cat[i]],c='r',label='men',linewidth=2)
    for key,spine in ax.spines.items():
        spine.set_visible(False)
    ax.set_xlim(1968,2011)
    ax.set_ylim(0,89)
    ax.set_title(major_cat[i])
    ax.tick_params(bottom='off',top='off',right='off',left='off')
    #ax.text(1970,12,'men')
    #ax.text(1970,75,'women')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()
