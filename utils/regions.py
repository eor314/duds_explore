import pandas as pd


def mbari_regions():
    """
    Returns MBARI defined regions in FathomNet
    """

    # this is the format for the command line tool
    regions = {'ca_borderland': '--max-latitude 35.38 --min-latitude 32.58 --max-longitude -117.2 --min-longitude -122.7',
            'davidson_seamount': '--max-latitude 35.9 --min-latitude 35.5  --max-longitude -122.5 --min-longitude -122.9',
            'eel_river': '--max-latitude 40.789 --min-latitude 40.07 --max-longitude -124.25 --min-longitude -125.105',
            'great_mb': '--max-latitude 37.199 --min-latitude 35.38 --max-longitude -121.0046 --min-longitude -123.8479',
            'gpg_seamounts': '--max-latitude 37.6 --min-latitude 36.82 --max-longitude -123.15 --min-longitude -123.61',
            'goc': '--max-latitude 32.37 --min-latitude 22.496 --max-longitude -106.498 --min-longitude -116.332',
            'hi': '--max-latitude 23.4 --min-latitude 18.25 --max-longitude -154.2 --min-longitude -161.27',
            'jdf': '--max-latitude 46.16 --min-latitude 44.3 --max-longitude -129.75 --min-longitude -130.67',
            'mars': '--max-latitude 36.714 --min-latitude 36.707 --max-longitude -122.182 --min-longitude -122.192',
            'mb': '--max-latitude 37.0538 --min-latitude 36.4458 --max-longitude -121.7805 --min-longitude -122.5073',
            'pac_nw': '--max-latitude 52.35 --min-latitude 39.7 --max-longitude -123.1 --min-longitude -131.9',
            'rqz_seamount': '--max-latitude 34.19 --min-latitude 33.865 --max-longitude -120.86 --min-longitude -121.26',
            'station_m': '--max-latitude 35.2521 --min-latitude 35.0375 --max-longitude -122.8026 --min-longitude -123.1858',
            'taney_seamount': '--max-latitude 36.95 --min-latitude 36.5 --max-longitude -124.745 --min-longitude -124.945',
            'vance_seamount': '--max-latitude 45.76 --min-latitude 45.155 --max-longitude -130.21 --min-longitude -131.0'
            }

    # convert that to dataframe
    regions_df = pd.DataFrame(index=regions.keys(), columns=['max-latitude', 'min-latitude', 'max-longitude', 'min-longitude'])

    for ii, jj in regions_df.iterrows():
        for j in jj.index.to_list():
            regions_df.at[ii, j] = float(regions[ii].split(j)[1].split(' ')[1])

    return regions, regions_df