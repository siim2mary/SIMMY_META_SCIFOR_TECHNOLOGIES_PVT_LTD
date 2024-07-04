import streamlit as st
import pandas as pd

st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

import streamlit as st
import numpy as np

dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)

st.title("Used styler")

import streamlit as st
import numpy as np
import pandas as pd

dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(dataframe.style.highlight_max(axis=0))

st.title("Used table as static method")
import streamlit as st
import numpy as np
import pandas as pd

dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))
st.table(dataframe)

st.title("Draw a line chart using st.line_chart")
import streamlit as st
import numpy as np
import pandas as pd

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

#Plot a map
#With st.map() you can display data points on a map. Let's use Numpy to generate some sample data and plot it on a map of San Francisco.

st.title("To display data points on a map using st.map")
import streamlit as st
import numpy as np
import pandas as pd

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

#Widgets
#When you've got the data or model into the state that you want to explore, 
# you can add in widgets like st.slider(), st.button() or st.selectbox(). It's really straightforward — treat widgets as variables:

st.title("Use widgets like st.slider,st.button, st,selectbox")
import streamlit as st
x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)

#Widgets can also be accessed by key, if you choose to specify a string to use as the unique key for the widget:
st.title("if you want to add a name ")
import streamlit as st
st.text_input("Your name", key="name")

# You can access the value at any point with:
st.session_state.name

#Use checkboxes to show/hide data
#One use case for checkboxes is to hide or show a specific chart or section in an app. 
# st.checkbox() takes a single argument, which is the widget label. In this sample, the checkbox is used to toggle a conditional statement.

st.title("Use checkbox to hide data or show specific chart st.checkbox")
import streamlit as st
import numpy as np
import pandas as pd

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data

st.title("USE selectbox")
#Use a selectbox for options
#Use st.selectbox to choose from a series. You can write in the options you want, or pass through an array or data frame column.

#Let's use the df data frame we created earlier.
import streamlit as st
import pandas as pd

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option

st.title("Layout, To add a box on left panel")
#Streamlit makes it easy to organize your widgets in a left panel sidebar with st.sidebar. 
# Each element that's passed to st.sidebar is pinned to the left, 
# allowing users to focus on the content in your app while still having access to UI controls.
#if you want to add a selectbox and a slider to a sidebar, 
# use st.sidebar.slider and st.sidebar.selectbox instead of st.slider and st.selectbox:
import streamlit as st

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)

#Beyond the sidebar, Streamlit offers several other ways to control the layout of your app.
#  st.columns lets you place widgets side-by-side, and st.expander lets you conserve space by hiding away large content.
import streamlit as st

left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
left_column.button('Press me!')

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")

#Show progress
#When adding long running computations to an app, you can 
# use st.progress() to display status in real time.

#First, let's import time. We're going to use the time.sleep() method to simulate a long running computation:
import streamlit as st
import time

'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)