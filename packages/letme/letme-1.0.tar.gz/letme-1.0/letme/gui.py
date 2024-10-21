import panel as pn

def simple(df):
    tabulator_editors = {}
    for column in df.columns:
        tabulator_editors[f'{column}'] = None

    return pn.widgets.Tabulator(
        df,
        layout='fit_columns',
        header_align='center',
        text_align='left',
        pagination='remote',
        page_size=5,
        sizing_mode='stretch_width',
        show_index=False,
        selectable=False,
        editors=tabulator_editors
    )