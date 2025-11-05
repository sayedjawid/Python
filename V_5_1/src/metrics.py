import pandas as pd

def total_loans(df: pd.DataFrame) -> int:
    return df['loan_id'].nunique()


def avg_loan_days(df: pd.DataFrame) -> float:
    return float(df['loan_days'].mean())


def overdue_rate(df: pd.DataFrame) -> float:
    return float((df['overdue_days'] > 0).mean())

def loans_by_genre(df: pd.DataFrame) -> pd.DataFrame:
    """delar upp raderna per genre och räknar lån i varje grupp"""
    return (
        df.groupby('genre', dropna=False)['loan_id']
        .nunique()
        .sort_values(ascending=False)
        .reset_index(name='loans')
    )

def loans_by_branch(df: pd.DataFrame) -> pd.DataFrame:
    """delar upp raderna per branch och räknar lån i varje grupp"""
    return (
        df.groupby('branch', dropna=False)['loan_id']
        .nunique()
        .sort_values(ascending=False)
        .reset_index(name='loans')
    )