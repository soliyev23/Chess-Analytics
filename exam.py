import streamlit as st
import pandas as pd 
from datetime import datetime
import string
import random
from streamlit_option_menu import option_menu
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("chess_dataset.csv")
# df = df.drop(columns="Unnamed: 0")/

df = df.rename(columns={"Unnamed: 2" : "rated"})


# Sidebarni to'girlash:
st.set_page_config(layout="wide", page_title="GamersData", page_icon="*")
with st.sidebar:
    # st.sidebar.title("Chess")
    st.sidebar.image("https://i.pinimg.com/originals/f6/b6/6e/f6b66e6a1991498318f7c64c10bb58f2.jpg")
    selected = option_menu(menu_title=None,options=["DataFrame haqida", "Missing value", "Grafik tahlil" ],default_index=0,)

if st.sidebar.button('Celebrate!'):
    st.balloons()





# Home
if selected == "DataFrame haqida":

    st.title("Assalomu Alaykum \"web application\"- ga hush kelibsiz 🤗")
    st.dataframe(df)

    st.write("## Bugun sizlar bilan shaxmat haqidagi malumotlarni ko'rib chiqamiz.")
    st.image("https://i.pinimg.com/originals/2e/7e/e5/2e7ee58125c4b42cc7387887eb350580.jpg")

    st.write("## Berilgan DataFrame dagi qiziqarli statistik ma'lumotlar.")



    column_1, column_2 = st.columns(2)

    with column_1:
        st.title("Rated or No?")
        # st.write()
        st.bar_chart(df.value_counts("rated",normalize=True)*100)
    with column_2:
        st.title("Who win?")
        # st.write()
        st.bar_chart(df.value_counts("winner",normalize=True)*100)

    st.title("The End of game.")
    st.bar_chart(df.value_counts("victory_status",normalize=True)*100)

    # st.subheader('')
    # with st.expander("HERE WE GO -----> "):
    #     st.write('Here we goooooo!')
    #     st.image("https://i.pinimg.com/originals/35/88/dc/3588dc1b2b72593f202427ab529ef890.jpg")




# Missin values
if selected == "Missing value":
    st.title("Bu yerda DataFrame ni clean qilamiz")
    st.dataframe(df)

    if st.button('Delete Column'):
        df = df.drop(columns="Unnamed: 0")
        st.dataframe(df)
    else:
        df = df.drop(columns="Unnamed: 0")

    st.write("## Count of Nan")

    st.bar_chart(df.isna().sum())

    st.subheader('')
    with st.expander("## ID column:"):

    # Id nan qiymatlar orniga yangi id 
        st.write(f"Count of NaN: {df['id'].isna().sum()}")
        st.write(df[df["id"].isna()].head(2))

        def generate_random_string(length=8):
            characters = string.ascii_letters + string.digits
            random_string = ''.join(random.choice(characters) for _ in range(length))
            return random_string

        df["id"] = df["id"].apply(lambda x: generate_random_string(8) if pd.isna(x) else x)


    # Generate randome ni dashboard ga chiqarish
        def read_code(file_path, start_line, end_line):
            with open(file_path, 'r') as file:
                lines = file.readlines()
                return ''.join(lines[start_line:end_line])
        file_path = 'exam.py'
        start_line = 87
        end_line = 94

        code_snippet = read_code(file_path, start_line, end_line)

        st.code(code_snippet, language='python')

        st.write(f"Count of Nan: {df['id'].isna().sum()}")



    # Dublicate larni ochirish 

        st.write(f"Dublicated:  {df.duplicated().sum()}")
        st.write(df[df["id"] == "kWKvrqYL"])

        df = df.drop_duplicates(subset="id")

        st.code(read_code(file_path, 117,119),language="python")

        st.write(f"Dublicated:  {df.duplicated().sum()}")

#---NUMERIC COLUMN------------------------------------------------------------------------------------------

    # multiselect_choice = st.sidebar.multiselect('Multiselect', ['Mean', 'Median', 'Mode'])

    temp2 = df.select_dtypes("number").fillna(df.select_dtypes("number").median())


    st.title("Numeric columns")

    tab1, tab2, tab3 = st.tabs(["Mean","Median","Mode"])

    lst = df.select_dtypes("number").columns
    temp = df.select_dtypes("number") 



    with tab1:
        df_1 = df.groupby(by=["victory_status"])[lst].transform(lambda x: x.fillna(x.mean()))
        df_1 = df_1.transform(lambda x: x.fillna(x.mean()))
        st.write(df_1.describe()-temp.describe())
    with tab2:
        df_2 = df.groupby(by=["victory_status"])[lst].transform(lambda x: x.fillna(x.median()))
        df_2 = df_2.transform(lambda x: x.fillna(x.mean()))
        st.write(df_2.describe()-temp.describe())
    with tab3:
        df_3 = df.groupby(by=["victory_status"])[lst].transform(lambda x: x.fillna(x.mode()))
        df_3 = df_3.transform(lambda x: x.fillna(x.mean()))
        st.write(df_3.describe()-temp.describe())

    st.code(read_code(file_path, 139,152),language="python")


    col1,col2 = st.columns(2)
    with col1:
        radio_choice = st. radio('Chose one of', ['Mean', 'Median', 'Mode'])
        if radio_choice == "Mean":
            pass
        if radio_choice == "Median":
            pass
        if radio_choice == "Mode":
            pass

        if st.button("Submit"):
            if radio_choice == "Mean":
                df[lst] = df.groupby(by=["victory_status"])[lst].transform(lambda x: x.fillna(x.mean()))
                df[lst] = df[lst].transform(lambda x: x.fillna(x.mean()))

                st.write('<p style="color:green; font-size:35px"> The Nan values is changed to MEAN</p>',unsafe_allow_html=True)

            elif radio_choice == "Median":
                df[lst] = df.groupby(by=["victory_status"])[lst].transform(lambda x: x.fillna(x.median()))
                df[lst] = df[lst].transform(lambda x: x.fillna(x.mean()))
                st.write('<p style="color:green; font-size:35px"> The Nan values is changed to MEDIAN</p>',unsafe_allow_html=True)

            else:
                df[lst] = df.groupby(by=["victory_status"])[lst].transform(lambda x: x.fillna(x.mode()))
                df[lst] = df[lst].transform(lambda x: x.fillna(x.mean()))
                st.write('<p style="color:green; font-size:35px"> The Nan values is changed to MODE</p>',unsafe_allow_html=True)
    with col2:
        st.subheader('')
        with st.expander("Numeric isna:"):
            st.write(df[lst].isna().sum())


#---OBJECT COLUMN------------------------------------------------------------------------------------------
    st.title("Object columns")
    obj_column = ["victory_status","winner","increment_code","white_id","black_id","moves","opening_eco","opening_name"]
    st.dataframe(df[obj_column])



    df[obj_column] = df.groupby(by=["victory_status"])[obj_column].transform(lambda x: x.fillna(x.mode()[0]))
    df[obj_column] = df[obj_column].transform(lambda x: x.fillna(x.mode()[0]))

    st.code(read_code(file_path, 194,197),language="python")
    st.subheader('')
    with st.expander("Amount of Nan"):
        st.write(df[obj_column].isna().sum())

    st.title("Boolean columns")
    
    df["rated"] = df.groupby(by=["victory_status"])["rated"].transform(lambda x: x.fillna(x.mode()[0]))
    df["rated"] = df["rated"].transform(lambda x: x.fillna(x.mode()[0]))

    st.code(read_code(file_path, 204,207),language="python")
    
    with st.expander("Amount of Nan"):
        st.write(df.isna().sum())



# TAHLIL FRAFIKALAR
if selected == "Grafik tahlil":
    st.title('Chess Games Analysis')

    # Distribution of game results over time
    st.header('Distribution of Game Results Over Time')
    df['created_at'] = pd.to_datetime(df['created_at'], unit='ms')
    games_per_month = df.groupby(df['created_at'].dt.to_period('M')).size()

    fig,ax = plt.subplots(figsize=(10, 6))
    games_per_month.plot(kind='line',color="r",ax=ax,style="--")
    ax.grid()
    ax.set_xlabel('Time')
    ax.set_ylabel('Number of Games')
    st.pyplot(plt)

    st.header('Number of Games Won by White vs. Black')
    winner_counts = df['winner'].value_counts()
    fig,ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x=winner_counts.index, y=winner_counts.values, palette='viridis',ax=ax)
    ax.set_xlabel('Winner')
    ax.set_ylabel('Number of Games')
    st.pyplot(plt)

    # Distribution of game durations
    st.header('Distribution of Game Durations (Turns)')

    col1,col2 = st.columns(2)
    with col1:
        bin = st.select_slider(
        "select bin number",
        options=list(range(1, 30)))
    
    with col2:
        color_picker_value = st.color_picker('Color picker')

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(df['turns'], bins=bin, kde=True,ax=ax,color=color_picker_value)
    ax.set_xlabel('Number of Turns')
    ax.set_ylabel('Frequency')
    st.pyplot(plt)
    


    # Distribution of game durations for different victory statuses
    st.header('Distribution of Game Durations for Different Victory Statuses')
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(data=df, x='turns', hue='victory_status', multiple='stack', bins=30)
    ax.set_xlabel('Number of Turns')
    ax.set_ylabel('Frequency')
    st.pyplot(plt)



    st.header('Most Common Openings')
    opening_counts = df['opening_name'].value_counts().head(10)
    fig,ax = plt.subplots(figsize=(12, 6))
    sns.barplot(y=opening_counts.index, x=opening_counts.values, palette='magma',ax=ax)
    ax.set_xlabel('Number of Games')
    ax.set_ylabel('Opening Name')
    st.pyplot(plt)


    white = df[df["winner"] == "white"]
    black = df[df["winner"] == "black"]
    
    st.header('Distribution of Player Ratings')

    fig,ax = plt.subplots(1,2, figsize=(12,6))

    sns.histplot(data=white, x="white_rating",ax=ax[0],bins=30,color="g")
    ax[0].set_title("White Rating")
    sns.histplot(data=black, x="black_rating",ax=ax[1],bins=30,color="Blue")
    ax[1].set_title("Black Rating")

    st.pyplot(fig)

    bin = st.select_slider(
    "select bin number",
    options=list(range(1, 85)))

    fig,ax = plt.subplots( figsize=(10,6))
    

    sns.histplot(data=white, x="white_rating", ax=ax,color="r",label="white_rating",bins=bin)
    sns.histplot(data=black, x="black_rating", ax=ax,color="Blue",label="black_rating",bins=bin)
    ax.legend()

    st.pyplot(fig)



    # Heatmap
    st.header('Heatmap of Correlations')
    
    options = st.multiselect('Select multiple options to display:',df.select_dtypes("number").columns,default="white_rating")

    
    correlation_matrix = df[options].corr()
    plt.figure(figsize=(10, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0)
    plt.title('Correlation Heatmap')
    st.pyplot(plt)






    











        

        



        






        



            
