'''
Created on 18 Oct 2024

@author: jacklok
'''
from trexanalytics.conf import BIGQUERY_GCLOUD_PROJECT_ID, MERCHANT_DATASET,\
    BIGQUERY_SERVICE_CREDENTIAL_PATH
import logging
from trexlib.utils.google.bigquery_util import create_bigquery_client,\
    execute_query
from trexlib.utils.log_util import get_tracelog
from datetime import datetime
from dateutil.relativedelta import relativedelta

logger = logging.getLogger('analytics')


def fetch_top_spender_data(date_range_from, date_range_to, limit=10, account_code=None, outlet_key=None,
                           min_total_spending_amount=.0, 
                           min_total_visit_amount = 0,
                           ):
    query = __prepare_top_spender_query(
                date_range_from, 
                date_range_to,
                limit                       = limit,
                account_code                = account_code,
                outlet_key                  = outlet_key,
                min_total_spending_amount   = min_total_spending_amount,
                min_total_visit_amount      = min_total_visit_amount,
                )
    bg_client       = create_bigquery_client(credential_filepath=BIGQUERY_SERVICE_CREDENTIAL_PATH)
    
    if bg_client is not None:
            logger.info('BigQuery Client is not none, thus going to execute query')
        
    try:
        job_result_rows = execute_query(bg_client, query)
        
        bg_client.close()
    except:
        job_result_rows = []
        logger.error('Failed to execute query due to %s', get_tracelog())
    
    row_list = []
    if job_result_rows:
        
        for row in job_result_rows:
            #logger.debug(row)
            column_dict = {}
            column_dict['customerKey']              = row.CustomerKey
            column_dict['totalTransactAmount']      = row.totalTransactAmount
            column_dict['transactionCount']         = row.transactionCount
            
            row_list.append(column_dict)
    
    return row_list

def fetch_non_active_customer_data(num_of_month, membership_key=None, tier_membership_key=None, limit=10, account_code=None, 
                           
                           ):
    query = __prepareTopSpenderQuery(
                date_range_from, 
                date_range_to,
                limit                       = limit,
                account_code                = account_code,
                outlet_key                  = outlet_key,
                min_total_spending_amount   = min_total_spending_amount,
                min_total_visit_amount      = min_total_visit_amount,
                )
    bg_client       = create_bigquery_client(credential_filepath=BIGQUERY_SERVICE_CREDENTIAL_PATH)
    
    if bg_client is not None:
            logger.info('BigQuery Client is not none, thus going to execute query')
        
    try:
        job_result_rows = execute_query(bg_client, query)
        
        bg_client.close()
    except:
        job_result_rows = []
        logger.error('Failed to execute query due to %s', get_tracelog())
    
    row_list = []
    if job_result_rows:
        
        for row in job_result_rows:
            #logger.debug(row)
            column_dict = {}
            column_dict['customerKey']              = row.CustomerKey
            column_dict['totalTransactAmount']      = row.totalTransactAmount
            column_dict['transactionCount']         = row.transactionCount
            
            row_list.append(column_dict)
    
    return row_list
    

def __prepare_top_spender_query(date_range_from, date_range_to, 
                             limit=10, account_code=None, outlet_key=None,
                             min_total_spending_amount=.0, 
                             min_total_visit_amount = 0,
                             ):
    
        
    account_code = account_code.replace('-','')
    
    where_condition  = ''
    
    where_final_condition  = 'WHERE'
    
    if date_range_from and date_range_to:
        if outlet_key:
            where_condition = "WHERE _TABLE_SUFFIX BETWEEN '{date_range_from}' and '{date_range_to}' and TransactOutlet='{outlet_key}' and ".format(date_range_from=date_range_from, 
                                                                                                     date_range_to=date_range_to, outlet_key=outlet_key)
        else:
            where_condition = "WHERE _TABLE_SUFFIX BETWEEN '{date_range_from}' and '{date_range_to}' and ".format(date_range_from=date_range_from, 
                                                                                                     date_range_to=date_range_to)
    else:
        if outlet_key:
            where_condition = "WHERE TransactOutlet='{outlet_key}' and ".format(outlet_key=outlet_key)
        else:
            where_condition = "WHERE "
    
    if min_total_spending_amount>0:
        where_final_condition  = '%s totalTransactAmount>=%s' % (where_final_condition, min_total_spending_amount)
        
        if min_total_visit_amount>0:
            where_final_condition  = '%s and transactionCount>=%s' % (where_final_condition, min_total_visit_amount)
    else:
        if min_total_visit_amount>0:
            where_final_condition  = '%s transactionCount>=%s' % (where_final_condition, min_total_visit_amount)
        else:
            where_final_condition = ''
            
    query = '''
            SELECT CustomerKey, totalTransactAmount, transactionCount
                FROM (
                    SELECT CustomerKey, SUM(TransactAmount) as totalTransactAmount, count(*) as transactionCount
                    FROM (
                        
                        SELECT
                            CustomerKey,
                            TransactAmount, 
                            Reverted
                            
                          FROM
                               `{project_id}.{dataset_name}.customer_transaction_{account_code}_*`
                                
                                {where_condition}
                                IsSalesTransaction=true
                    )
                    WHERE Reverted=False
                    GROUP BY CustomerKey
                )
                {where_final_condition}       
                    order by totalTransactAmount desc
                    LIMIT {limit}
                    
                 
               
        '''.format(project_id=BIGQUERY_GCLOUD_PROJECT_ID, dataset_name=MERCHANT_DATASET, 
                   where_condition=where_condition,
                   where_final_condition=where_final_condition,
                   limit=limit,
                   account_code=account_code)    
        
    logger.debug('QueryMerchantOutletCustomerTopSpendingAmountByDateRange: query=%s', query)

    return query  

def __prepare_non_active_customer_query(
                                num_of_months, 
                                limit=10, account_code=None,
                                membership_key=None,
                                tier_membership_key=None,
                             ):
    
        
    account_code = account_code.replace('-','')
    
    where_final_condition  = 'WHERE'
    
    today = datetime.utcnow().date()
    
    from_date = today - relativedelta(months=num_of_months)
    
    date_range_from = datetime.strftime(from_date, '%Y%m%d')
    date_range_to   = datetime.strftime(today, '%Y%m%d')
    
    where_condition = "WHERE _TABLE_SUFFIX BETWEEN '{date_range_from}' and '{date_range_to}' and ".format(date_range_from=date_range_from, 
                                                                                                     date_range_to=date_range_to)
    
    query = '''
            SELECT CustomerKey, TransactDateTime
                FROM (
                    SELECT
                        checking_transaction.TransactDateTime as TransactDateTime, 
                        checking_transaction.UpdatedDateTime, 
                        checking_transaction.Reverted as Reverted
                        
                      FROM
                        (
                        SELECT
                           MAX(TransactDateTime) AS LatestTransactDateTime
                         FROM
                           `{project_id}.{dataset_name}.customer_transaction_{account_code}_*`
                            
                            {where_condition}
                            IsSalesTransaction=true
                    
                         
                      
                )
                {where_final_condition}       
                    
                    
                 
               
        '''.format(project_id=BIGQUERY_GCLOUD_PROJECT_ID, dataset_name=MERCHANT_DATASET, 
                   where_condition=where_condition,
                   where_final_condition=where_final_condition,
                   limit=limit,
                   account_code=account_code)    
        
    logger.debug('QueryMerchantOutletCustomerTopSpendingAmountByDateRange: query=%s', query)

    return query   
    
