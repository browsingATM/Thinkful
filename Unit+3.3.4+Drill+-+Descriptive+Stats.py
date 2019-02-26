
# coding: utf-8

# In[14]:


#Poisson
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')

poisson = np.random.poisson([5], 100)
plt.hist(poisson)
# Add a vertical line at the mean.
plt.axvline(poisson.mean(), color='r', linestyle='solid', linewidth=2)

# Add a vertical line at one standard deviation above the mean.

plt.axvline(poisson.mean() + poisson.std(), color='r', linestyle='dashed', linewidth=1)

# Add a vertical line at one standard deviation below the mean.
plt.axvline(poisson.mean() - poisson.std(), color='r', linestyle='dashed', linewidth=1) 

plt.show()


# In[15]:


#the mean and st dev are helpful indicatos to show where the data is skewed--non-normal distributions


# In[34]:


#Bernoulli
import numpy as mp
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')

plt.axvline(bern.mean(), color='r', linestyle='solid', linewidth=2)
plt.axvline(bern.mean() + bern.std(), color='r', linestyle='dashed', linewidth=1)
plt.axvline(bern.mean() - bern.std(), color='r', linestyle='dashed', linewidth=1)

bern = np.random.binomial(1, .5, 100)
plt.hist(bern)
plt.show()


# In[24]:


#in this case, the data is so hevaily split the mean and st. dev aren't that useful other than knowing where


# In[25]:


#there data slightly skews harder to one side.


# In[35]:


#Binomial
import numpy as mp
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')

plt.axvline(bern.mean(), color='r', linestyle='solid', linewidth=2)
plt.axvline(bern.mean() + bern.std(), color='r', linestyle='dashed', linewidth=1)
plt.axvline(bern.mean() - bern.std(), color='r', linestyle='dashed', linewidth=1)

binomial = np.random.binomial(12, .9, 100)

# Plot a histogram.
plt.hist(binomial)

# Print the histogram.
plt.show()


# In[37]:


#Gamma
import numpy as mp
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')

plt.axvline(gamma.mean(), color='r', linestyle='solid', linewidth=2)
plt.axvline(gamma.mean() + gamma.std(), color='r', linestyle='dashed', linewidth=1)
plt.axvline(gamma.mean() - gamma.std(), color='r', linestyle='dashed', linewidth=1)

gamma = np.random.gamma(5,1, 100)
plt.hist(gamma)
plt.show()


# In[ ]:


#yes, the mean and st dev shows where the data clusters

