import inflection
if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):

    # Specify your transformation logic here
    print("Number of rows of our dataset is ",data.shape)

    

    print("Data where the number of passengers was 0 is", data[data["passenger_count"]==0].shape )

    print("Data where the number of trip_distance was 0 is", data[data["trip_distance"]==0].shape )

    print(data[(data["passenger_count"]!=0) & (data["trip_distance"]!=0) ].shape)
    # data = data[data["passenger_count"]>0]
    # data = data[data["trip_distance"]>0]
    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date

    #original column names
    original_columns = data.columns
    data.columns =data.columns.map(inflection.underscore).str.lower()
    modified_columns = data.columns
    num_converted_columns = sum(original != modified for original, modified in zip(original_columns, modified_columns))

    print(f"Number of columns converted to snake case: {num_converted_columns}")
    print(data.vendor_id.unique())

    return data[(data["trip_distance"]>0) & (data["passenger_count"]>0)]#data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    # assert output is not None, 'The output is undefined'
    assert (output["trip_distance"].isin([0]).sum()==0)  
    assert (output["passenger_count"].isin([0]).sum()==0) # ,   'There are rides with no zero Trip distance'
    assert output.vendor_id.unique() in [1,2,3]
