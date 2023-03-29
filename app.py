import streamlit as st
import numpy as np
import pandas as pd 
import sklearn

import pickle 

model_1 = pickle.load(open('model.sav','rb'))
from PIL import Image 
def run_this():
    st.title('welcome! Borrower :boy:')
    img1 =Image.open('image.jpg')
    img1 = img1.resize((450,245))
    st.image(img1,use_column_width=False)

    st.sidebar.header('About')
    st.sidebar.text('''In this paper, we study the borrower-, loan- and social- related determinants 
of performance predictability in an online P2P lending market by 
conceptualizing financial and social strength to predict whether the 
borrowers could be funded with lower interest, and the lenders would be 
timely paid''')

    st.text('When you default on a loan, your account is sent to a debt collection agency that tries to recover your outstanding payments')
    # image login
    img2 =Image.open('image2.jpg')
    img2 = img2.resize((200,75))
    st.image(img2,use_column_width=False)
    
    st.text_input('Enter your name ')
    st.text_input(' Enter your city name ')
    st.text_input('Enter your contact number ')




     ### title

    st.title("Let's see your prosper rating :star: ")


    

    ## is homehoner 
    home_is =['Yes','No']
    
    home = st.selectbox("Are you a homeowner ?",home_is)
    if home=='Yes':
        home_owner=1
    else :
        home_owner=0
    # st.write('you are',home_owner)

    ###### loan status
    loan_is =['Accepted','HighRisk']
    
    loan = st.selectbox("Loan Status ?",loan_is)
    if loan=='Accepted':
        loan_sta=0
    else :
        loan_sta=1
    # st.write('your loan',loan_owner)
    
    ##### employment status
    occup =['Employed', 'Other', 'Full-time', 'Self-employed', 'Not employed',
       'Retired', 'Part-time']
    
    ocu = st.selectbox("Your enployment status  ?",occup)
    if ocu=='Employed':
        occupation=0
    if ocu=='Full-time':
        occupation =1
    if ocu=='Not employed':
        occupation =2
    if ocu=='Other':
        occupation =3
    if ocu=='Part-time':
        occupation =4
    if ocu=='Retired':
        occupation =5
    else :
        occupation =6
    ######

    borrow_amo=st.slider('How much ammount you are borrowing ?',0,4000)

    #####
    monthly_inco=st.slider('Your monthly income ?',0,4000)

    #####
    term =['12 month','36 month','60 month']
    
    To_term = st.selectbox("Term of loan in month ?",term)
    if To_term =='12 month':
        te=0
    if To_term =='36 month':
         te=1
    else :
        te=2

    
        
    #####
    income_varify =['Yes','No']
    
    ve = st.selectbox("Your income varified by any officer ?",income_varify)
    if ve=='Yes':
        vari=1
    else :
        vari=0
    ##### running loan
    loan_rin =['Yes','No']
    
    loan_l = st.selectbox("Any current loan ?",loan_rin)
    if loan_l=='Yes':
        loni=1
    else :
        loni=0
    



    ##### category 

    catego= {'Auto': 0, 'Baby & Adoption': 1, 'Boat': 2, 'Business': 3, 'Cosmetic Procedure': 4, 'Debt Consolidation': 5, 'Engagement Ring': 6, 'Green Loans': 7, 'Home Improvement': 8, 'Household Expenses': 9, 'Large Purchases': 10, 'Medical or Dental': 11, 'Motorcycle': 12, 'Not Available': 13, 'Other': 14, 'RV': 15, 'Student Use': 16, 'Taxes': 17, 'Vacation': 18, 'Wedding Loans': 19}


    cate =['Home Improvement', 'Motorcycle', 'Debt Consolidation', 'Other',
       'Household Expenses', 'Auto', 'Medical or Dental', 'Wedding Loans',
       'Vacation', 'Taxes', 'Business', 'Baby & Adoption',
       'Engagement Ring', 'Large Purchases', 'Boat', 'RV',
       'Cosmetic Procedure', 'Not Available', 'Student Use',
       'Green Loans']
    
    ca = st.selectbox("Your loan will be for (item)  ?",cate)
    category_i=catego[ca]
    # st.write('you want',category_i)



    stat= { 'AL': 1, 'AR': 2, 'AZ': 3, 'CA': 4, 'CO': 5, 'CT': 6, 'DC': 7, 'DE': 8, 'FL': 9, 'GA': 10, 'HI': 11, 'ID': 12 }
    sta= ['AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA','HI', 'ID']
    state = st.selectbox("In which state you live  ?",sta)
    st_i=stat[state]
    # st.write('you want',st_i)
    
    
   ############ income range 

    inc={'$0': 0, '$1-24,999': 1, '$100,000+': 2, '$25,000-49,999': 3, '$50,000-74,999': 4, '$75,000-99,999': 5}
    inco=['$50,000-74,999', '$25,000-49,999', '$100,000+', '$75,000-99,999', '$1-24,999', '$0']
    income = st.selectbox("your income range  ?",inco)
    inco_i=inc[income]
    # st.write('you want',inco_i)


   

    borrow_Apr=st.slider('Borrower APR ?',0,6000)

    borrow_dpi=st.slider('Dept to income ratio ?',0,6000)

    ######
    sub=st.button("SUBMIT")
    if sub:
        input_data =(category_i,st_i,home_owner,inco_i,vari,borrow_dpi,monthly_inco,te,occupation,loni,borrow_amo,borrow_Apr,loan_sta )
        input_data_as_numpy_array = np.asarray(input_data)

        # reshape the np array as we are predicting for one instance
        input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

        prediction = model_1.predict(input_data_reshaped)
        k=list(prediction)
        result=k[0]
        # result_s=str(result)
        our_result={0 : 'weaker', 1 : 'HR', 2 : 'E', 3 : 'D', 4 : 'C', 5 : 'B', 6 : 'A', 7 : 'AA'}
        final_r=our_result[result]

        st.write('Your rating out of 7:star: is   :',result)
        st.write('Your category is : ',final_r)
        if result>5:
            st.write("I think you are Rich your chance of approval of loan is 100% ")
        elif result>3:
            st.write("I think you are middle class your chance of approval of loan is 70%")
        else:
            st.write("you may get loan but chance of getting loan is 30%")


   
        
       

    
    
    
run_this()