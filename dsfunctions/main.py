class dsf:
    '''
    # Basic EDA can be summed down to:
    # Source: https://en.wikipedia.org/wiki/Exploratory_data_analysis#:~:text=In statistics%2C exploratory data analysis,modeling or hypothesis testing task.&text=EDA encompasses IDA.

    # First Initial Data Analysis (IDA):

    # Answer these 4 questions:

    # Check the quality of data

    # Check the quality of measurments

    # Do any type of initial transformations

    # Did the collected data fufill the intentions of the research design
    ## Eg: background and substantive variables are equally distributed within and across groups.
    ## Eg: check the success of the non-random sampling, by Checking if all subgroups in population are represented
    ## Eg: check for dropout

    # Then EDA:
    # Summarize their main characteristics, often with visual methods
    # EDA is mostly seeing what data can tell the user beyond formal modeling or hypothesis testing 
    # 
    # Typical Graphical EDA: 
    # Boxplot, Histogram, Multivariate Chart, Scatter Plots, Run Charts, Targeted Projection Pursuit
        '''
    
    def __init__:
        '''
        If I can think of any initial variables i would need, i can put them here
        '''
    
    def csv_import_check(self, ):
        '''
        import csv into dataframe
        Check for null
        Check for weird datatypes
        Check for numerical outliers
        '''
        pass

    def fancy_heatmap(self, df):
        '''
        Creates a much more organized looking heatmap
        This script was created by someone online and shared in my dsir-824 class
        I did not make this, but i am implementing it here
        '''
        mask = np.zeros_like(df.corr())
        mask[np.triu_indices_from(mask)] = True

        plt.figure(figsize=(20, 10))
        sns.heatmap(
            df.corr(),
            #cmap='coolwarm',
            annot=True,
            mask = mask
        );
    