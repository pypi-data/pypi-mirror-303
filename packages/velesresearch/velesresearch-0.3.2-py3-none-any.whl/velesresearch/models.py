"""Classes for basic structural elements for SurveyJS"""

import json
import os
import shutil
import subprocess
import re
from pathlib import Path
from importlib.resources import files
from markdown import markdown
from pydantic import BaseModel, model_validator, Field
from .validators import ValidatorModel
from .utils import dict_without_defaults


class QuestionModel(BaseModel):
    """General question object model

    Attributes:
        name (str): The label of the question.
        title (str | None): The visible title of the question. If None, `name` is used.
        titleLocation (str): The location of the title. Can be 'default', 'top', 'bottom', 'left', 'hidden'.
        description (str | None): Optional subtitle or description of the question.
        descriptionLocation (str): The location of the description. Can be 'default', 'underTitle', 'underInput'.
        isRequired (bool): Whether the question is required.
        readOnly (bool): Whether the question is read-only.
        visible (bool): Whether the question is visible.
        requiredIf (str | None): Expression to make the question required.
        enableIf (str | None): Expression to enable the question.
        visibleIf (str | None): Expression to make the question visible.
        validators (ValidatorModel | list[ValidatorModel] | None): Validator(s) for the question.
        showOtherItem (bool): Whether to show the 'Other' item. Doesn't work with `showCommentArea`.
        showCommentArea (bool): Whether to show the comment area. Doesn't work with `showOtherItem`.
        commentPlaceholder (str | None): Placeholder text for the comment area.
        commentText (str | None): Text for the comment area.
        correctAnswer (str | None): Correct answer for the question. Use for quizzes.
        defaultValue (str | None): Default value for the question.
        defaultValueExpression (str | None): Expression deciding the default value for the question.
        requiredErrorText (str | None): Error text if the required condition is not met.
        errorLocation (str | None): Location of the error text. Can be 'default' 'top', 'bottom'.
        hideNumber (bool): Whether to hide the question number.
        id (str | None): HTML id attribute for the question. Usually not necessary.
        maxWidth (str): Maximum width of the question in CSS units.
        minWidth (str): Minimum width of the question in CSS units.
        resetValueIf (str | None): Expression to reset the value of the question.
        setValueIf (str | None): Expression with a condition to set the value of the question. Requires `setValueExpression`.
        setValueExpression (str | None): Expression to decide on the value of the question to be set. Requires `setValueIf`.
        startWithNewLine (bool): Whether to start the question on a new line.
        state (str | None): If the question should be collapsed or expanded. Can be 'default', 'collapsed', 'expanded'.
        useDisplayValuesInDynamicTexts (bool): Whether to use display names for question values in placeholders.
        width (str): Width of the question in CSS units.
        addCode (dict | None): Additional code for the question. Usually not necessary.
        customCode (str | None): Custom JS commands to be added to the survey.
        customFunctions (str | None): Custom JS functions definitions to be added to the survey. To be used with `customCode`.
    """

    name: str
    title: str | None = None
    type: str
    titleLocation: str = "default"
    description: str | None = None
    descriptionLocation: str = "default"
    isRequired: bool = False
    readOnly: bool = False
    visible: bool = True
    requiredIf: str | None = None
    enableIf: str | None = None
    visibleIf: str | None = None
    validators: ValidatorModel | list[ValidatorModel] | None = None
    showOtherItem: bool = False
    showCommentArea: bool = False
    commentPlaceholder: str | None = None
    commentText: str | None = None
    correctAnswer: str | None = None
    defaultValue: str | None = None
    defaultValueExpression: str | None = None
    requiredErrorText: str | None = None
    errorLocation: str = "default"
    hideNumber: bool = False
    id: str | None = None
    maxWidth: str = "100%"
    minWidth: str = "300px"
    resetValueIf: str | None = None
    setValueIf: str | None = None
    setValueExpression: str | None = None
    startWithNewLine: bool = True
    state: str = "default"
    useDisplayValuesInDynamicTexts: bool = True
    width: str = ""
    addCode: dict | None = None
    customCode: str | None = None
    customFunctions: str | None = None

    def __str__(self) -> str:
        return f"  {self.name} ({self.type}): {self.title}"

    def dict(self) -> dict:
        if self.validators is not None:
            if isinstance(self.validators, list):
                validators = {
                    "validators": [validator.dict() for validator in self.validators]
                }
            else:
                validators = {"validators": [self.validators.dict()]}
        else:
            validators = {}

        if self.addCode is not None:
            addCode = self.addCode
        else:
            addCode = {}
        return dict_without_defaults(self) | validators | addCode


class QuestionSelectBase(QuestionModel):
    """Base class for select type question object models

    Attributes:
        choices (str | dict | list): The choices for the question. Can be string(s) or dictionary(-ies) with structure `{"value": ..., "text": ...}`. You can also add `visibleIf`, `enableIf`, and `requiredIf` to the dictionary.
        choicesFromQuestion (str | None): The name of the question to get the choices from if the are to be copied. Use with `choicesFromQuestionMode`.
        choicesFromQuestionMode (str): The mode of copying choices. Can be 'all', 'selected', 'unselected'.
        choicesOrder (str): The order of the choices. Can be 'none', 'asc', 'desc', 'random'.
        showDontKnowItem: bool = False
        dontKnowText: str | None = None
        hideIfChoicesEmpty: bool | None = None
        showNoneItem: bool = False
        noneText: str | None = None
        showOtherItem: bool = False
        otherText: str | None = None
        otherErrorText: str | None = None
        showRefuseItem: bool = False
        refuseText: str | None = None
    """

    choices: str | dict | list
    choicesFromQuestion: str | None = None
    choicesFromQuestionMode: str = "all"
    choicesOrder: str = "none"
    showDontKnowItem: bool = False
    dontKnowText: str | None = None
    hideIfChoicesEmpty: bool | None = None
    showNoneItem: bool = False
    noneText: str | None = None
    showOtherItem: bool = False
    otherText: str | None = None
    otherErrorText: str | None = None
    showRefuseItem: bool = False
    refuseText: str | None = None


class QuestionDropdownModel(QuestionSelectBase):
    """A dropdown type question object model

    Attributes:
        choicesMax (int | None): Maximum for automatically generated choices. Use with `choicesMin` and `choicesStep`.
        choicesMin (int | None): Minimum for automatically generated choices. Use with `choicesMax` and `choicesStep`.
        choicesStep (int | None): Step for automatically generated choices. Use with `choicesMax` and `choicesMin`.
        placeholder (str | None): Placeholder text.
    """

    choicesMax: int | None = None
    choicesMin: int | None = None
    choicesStep: int | None = None
    placeholder: str | None = None
    type: str = Field(default="dropdown")


class QuestionTextBase(QuestionModel):
    """Base class for text type question object models

    Attributes:
        monitorInput (bool): Whether to count the time spent with the question focused and the number of key presses. Useful for bot detection.
    """

    monitorInput: bool = False


class QuestionTextModel(QuestionTextBase):
    """A short text type question object model

    Attributes:
        autocomplete (str | None): A value of `autocomplete` attribute for `<input>`. See MDN for a list: <https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/autocomplete#token_list_tokens>.
        inputType (str | None): The type of the input. Can be 'text', 'password', 'email', 'url', 'tel', 'number', 'date', 'datetime-local', 'time', 'month', 'week', 'color'.
        max (str): The `max` attribute of `<input>`. Syntax depends on the `inputType`. See MDN for details: <https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/max>.
        maxErrorText (str | None): Error text if the value exceeds `max`.
        maxLength (int | None): The maximum length of the input in characters. Use 0 for no limit. Use -1 for the default limit.
        maxValueExpression (str | None): Expression to decide the maximum value.
        min (str | int | None): The `min` attribute of `<input>`. Syntax depends on the `inputType`. See MDN for details: <https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/min>.
        minErrorText (str | None): Error text if the value is less than `min`.
        minValueExpression (str | None): Expression to decide the minimum value.
        placeholder (str | None): Placeholder text for the input.
        size (int | None): The width of the input in characters. A value for `size` attribute of `<input>`.
        step (str | None): The `step` attribute of `<input>`. Syntax depends on the `inputType`. See MDN for details: <https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/step>.
        textUpdateMode (str): The mode of updating the text. Can be 'default', 'onBlur' (update after the field had been unclicked), 'onTyping' (update every key press).
    """

    autocomplete: str | None = None
    inputType: str = "text"
    max: str | int | None = None
    maxErrorText: str | None = None
    maxLength: int | None = None
    maxValueExpression: str | None = None
    min: str | int | None = None
    minErrorText: str | None = None
    minValueExpression: str | None = None
    placeholder: str | None = None
    size: int | None = None
    step: str | None = None
    textUpdateMode: str = "default"
    type: str = Field(default="text")


class QuestionCheckboxBase(QuestionSelectBase):
    """Base class for checkbox type question object models

    Attributes:
        colCount (int | None): The number of columns for the choices. 0 means a single line.
    """

    colCount: int | None = None


class QuestionCheckboxModel(QuestionCheckboxBase):
    """A checkbox type question object model

    Attributes:
        isAllSelected (bool | None): Start with all choices selected. Default is False.
        maxSelectedChoices (int): Maximum number of selected choices. 0 means no limit.
        minSelectedChoices (int): Minimum number of selected choices. 0 means no limit.
        selectAllText (str | None): Text for the 'Select All' item.
        showSelectAllItem (bool | None): Whether to show the 'Select All' item.
    """

    isAllSelected: bool | None = None
    maxSelectedChoices: int = 0
    minSelectedChoices: int = 0
    selectAllText: str | None = None
    showSelectAllItem: bool | None = None
    type: str = Field(default="checkbox")


class QuestionRankingModel(QuestionCheckboxModel):
    """A ranking type question object model

    Attributes:
        longTap (bool): Whether to use long tap for dragging on mobile devices.
        selectToRankAreasLayout (str): The layout of the ranked and unranked areas when `selectToRankEnabled=True`. Can be 'horizontal', 'vertical'.
        selectToRankEmptyRankedAreaText (str | None): Text for the empty ranked area when `selectToRankEnabled=True`.
        selectToRankEmptyUnrankedAreaText (str | None): Text for the empty unranked area when `selectToRankEnabled=True`.
        selectToRankEnabled (bool): Whether user should select items they want to rank before ranking them. Default is False.
    """

    longTap: bool = True
    selectToRankAreasLayout: str = "horizontal"
    selectToRankEmptyRankedAreaText: str | None = None
    selectToRankEmptyUnrankedAreaText: str | None = None
    selectToRankEnabled: bool = False

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.type = "ranking"


class QuestionRadiogroupModel(QuestionCheckboxBase):
    """A radiogroup type question object model

    Attributes:
        showClearButton (bool): Show a button to clear the answer.
    """

    showClearButton: bool = False
    type: str = Field(default="radiogroup")

    def __str__(self):
        string = super().__str__() + "\n"
        for i, choice in enumerate(self.choices):
            string += f"    {i + 1}. {choice}\n"
        return string


class QuestionTagboxModel(QuestionCheckboxModel):
    """A multiselect dropdown type question object model

    Attributes:
        allowClear (str): Whether to show the 'Clear' button for each answer.
        closeOnSelect (int | None): Whether to close the dropdown after user selects a specified number of items.
        hideSelectedItems (bool | None): Whether to hide selected items in the dropdown.
        placeholder (str | None): Placeholder text for the input with no value.
        searchEnabled (bool): Whether to enable search in the dropdown.
        searchMode (str): The search mode. Can be 'contains' (default), 'startsWith'. Works only if `searchEnabled=True`.
    """

    allowClear: bool = True
    closeOnSelect: int | None = None
    hideSelectedItems: bool | None = False
    placeholder: str | None = None
    searchEnabled: bool = True
    searchMode: str = "contains"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.type = "tagbox"


class QuestionCommentModel(QuestionTextBase):
    """A long text type question object model

    Attributes:
        acceptCarriageReturn (bool): Whether to allow line breaks. Default is True.
        allowResize (bool): Whether to allow resizing the input field. Default is True.
        autoGrow (bool): Whether to automatically grow the input field. Default is False.
        rows (int): Height of the input field in rows' number.
    """

    acceptCarriageReturn: bool = True
    allowResize: bool | None = None
    autoGrow: bool | None = None
    rows: int = 4
    type: str = Field(default="comment")


class QuestionRatingModel(QuestionModel):
    """A rating type question object model

    Attributes:
        maxRateDescription (str | None): Description for the biggest rate.
        minRateDescription (str | None): Description for the smallest rate.
        rateMax (int): Maximum rate. Works only if `rateValues` is not set.
        rateMin (int): Minimum rate. Works only if `rateValues` is not set.
        rateStep (int): Step for the rate. Works only if `rateValues` is not set.
        rateType (str): The type of the rate. Can be 'labels', 'stars', 'smileys'.
        rateValues (list | None): Manually set rate values. Use a list of primitives and/or dictionaries `{"value": ..., "text": ...}`.
        scaleColorMode (str): The color mode of the scale if `rateType='smileys'`. Can be 'monochrome', 'colored'.
    """

    maxRateDescription: str | None = None
    minRateDescription: str | None = None
    rateMax: int = 5
    rateMin: int = 1
    rateStep: int = 1
    rateType: str = "labels"
    rateValues: list | None = None
    scaleColorMode: str = "monochrome"
    type: str = Field(default="rating")


class QuestionImagePickerModel(QuestionModel):
    """An image picker type question object model"""

    type: str = Field(default="imagepicker")

    # TODO


class QuestionBooleanModel(QuestionModel):
    """A yes/no type question object model

    Attributes:
        labelFalse (str | None): Label for the 'false' value.
        labelTrue (str | None): Label for the 'true' value.
        swapOrder (bool): Whether to swap the default (no, yes) order of the labels.
        valueFalse (str): Value for the 'false' option.
        valueTrue (str): Value for the 'true' option.
    """

    labelFalse: str | None = None
    labelTrue: str | None = None
    swapOrder: bool = False
    valueFalse: bool | str = False
    valueTrue: bool | str = True
    type: str = Field(default="boolean")


class QuestionImageModel(QuestionModel):
    """An image type question object model

    Attributes:
        altText (str | None): The alt property for <img>.
        contentMode (str): The content type. Can be 'auto' (default), 'image', 'video', 'youtube'.
        imageFit (str): The object-fit property of <img>. Can be 'contain', 'cover', 'fill', 'none'. See MDN <https://developer.mozilla.org/en-US/docs/Web/CSS/object-fit>.
        imageHeight (int | str): The height of the image container in CSS units. See `imageFit`.
        imageLink (str | None): The src property for <img> or video link.
        imageWidth (int | str): The width of the image container in CSS units. See `imageFit`.
    """

    altText: str | None = None
    contentMode: str = "auto"
    imageFit: str = "contain"
    imageHeight: int | str = 150
    imageLink: str | None = None
    imageWidth: int | str = 200
    type: str = Field(default="image")


class QuestionHtmlModel(QuestionModel):
    """An info type question object model

    Attributes:
        html (str): The HTML content of the infobox.
    """

    html: str
    type: str = Field(default="html")

    @model_validator(mode="before")
    def process_html(cls, values):
        # Automatically convert the `html` field to its markdown version
        if "html" in values:
            values["html"] = markdown(values["html"])
        return values

    def __str__(self):
        return f"  {self.name} ({self.type}): {self.html[:20]}…\n"


class QuestionSignaturePadModel(QuestionModel):
    """A signature pad type question object model"""

    type: str = Field(default="signaturepad")

    # TODO


class QuestionExpressionModel(QuestionModel):
    """An expression type question object model (read-only)"""

    type: str = Field(default="expression")

    # TODO


class QuestionFileModel(QuestionModel):
    """A file type question object model"""

    type: str = Field(default="file")

    # TODO


class QuestionMatrixBaseModel(QuestionModel):
    """Base for matrix type questions

    Attributes:
        columns (list | dict): The columns of the matrix. Use primitives or dictionaries `{"text": ..., "value": ..., "type": ..., "otherParameter": ...}`.
        rows (list | dict | None): The rows of the matrix. Use primitives or dictionaries `{"text": ..., "value": ...}`.
        alternateRows (bool | None): Whether to alternate the rows.
        columnMinWidth (str | None): Minimum width of the column in CSS units.
        displayMode (str): The display mode of the matrix. Can be 'auto', 'list', 'table'.
        rowTitleWidth (str | None): Width of the row title in CSS units.
        showHeader (bool): Whether to show the header of the table.
        verticalAlign (str): The vertical alignment of the content. Can be 'top', 'middle'.
    """

    columns: list | dict
    rows: list | dict | None = None
    alternateRows: bool | None = None
    columnMinWidth: str | None = None
    displayMode: str = "auto"
    rowTitleWidth: str | None = None
    showHeader: bool = True
    verticalAlign: str = "middle"

    def dict(self):
        if self.columns is not None:
            columns = {
                "columns": [
                    column.dict() if isinstance(column, QuestionModel) else column
                    for column in self.columns
                ]
            }
            for col in columns["columns"]:
                if isinstance(col, dict) and "type" in col:
                    col["cellType"] = col.pop("type")
        else:
            columns = {}

        if self.rows is not None:
            if not isinstance(self.rows, list):
                rows = [rows]
            rows = {"rows": self.rows}
        else:
            rows = {}

        if self.validators is not None:
            if isinstance(self.validators, list):
                validators = {
                    "validators": [validator.dict() for validator in self.validators]
                }
            else:
                validators = {"validators": [self.validators.dict()]}
        else:
            validators = {}

        if self.addCode is not None:
            addCode = self.addCode
        else:
            addCode = {}

        return dict_without_defaults(self) | columns | rows | validators | addCode


class QuestionMatrixDropdownModelBase(QuestionMatrixBaseModel):
    """Base for matrix dropdown type questions

    Attributes:
        cellErrorLocation (str): The location of the error text for the cells. Can be 'default', 'top', 'bottom'.
        cellType (str | None): The type of the matrix cells. Can be overridden for individual columns. Can be "dropdown" (default), "checkbox", "radiogroup", "tagbox", "text", "comment", "boolean", "expression", "rating".
        choices (str | dict | list | None): The default choices for all select questions. Can be overridden for individual columns. Can be string(s) or dictionary(-ies) with structure `{"value": ..., "text": ..., "otherParameter": ...}`.
        isUniqueCaseSensitive (bool): Whether the case of the answer should be considered when checking for uniqueness. If `True`, "Kowalski" and "kowalski" will be considered different answers.
        placeHolder (str | None): Placeholder text for the cells.
        transposeData (bool): Whether to show columns as rows. Default is False.
    """

    cellErrorLocation: str = "default"
    cellType: str | None = None
    choices: str | dict | list | None = None
    isUniqueCaseSensitive: bool = False
    placeHolder: str | None = None
    transposeData: bool = False


class QuestionMatrixModel(QuestionMatrixBaseModel):
    """A single-select matrix type question object model

    Attributes:
        eachRowUnique (bool | None): Whether each row should have a unique answer. Defaults to False.
        hideIfRowsEmpty (bool | None): Whether to hide the question if no rows are visible.
        isAllRowRequired (bool): Whether each and every row is to be required.
        rowsOrder (str): The order of the rows. Can be 'initial', 'random'.
    """

    eachRowUnique: bool | None = None
    hideIfRowsEmpty: bool | None = None
    isAllRowRequired: bool = False
    rowsOrder: str = "initial"
    type: str = Field(default="matrix")


class QuestionMatrixDropdownModel(QuestionMatrixDropdownModelBase):
    """A multi-select matrix type question object model"""

    type: str = Field(default="matrixdropdown")

    # TODO


class QuestionMatrixDynamicModel(QuestionMatrixDropdownModelBase):
    """A dynamic matrix type question object model

    Attributes:
        addRowLocation (str): The location of the 'Add row' button. Can be 'default', 'top', 'bottom', 'topBottom' (both top and bottom).
        addRowText (str | None): Text for the 'Add row' button.
        allowAddRows (bool): Whether to allow adding rows.
        allowRemoveRows (bool): Whether to allow removing rows.
        allowRowsDragAndDrop (bool): Whether to allow dragging and dropping rows to change order.
        confirmDelete (bool): Whether to prompt for confirmation before deleting a row. Default is False.
        confirmDeleteText (str | None): Text for the confirmation dialog when `confirmDelete` is True.
        defaultRowValue (str | None): Default value for the new rows that has no `defaultValue` property.
        defaultValueFromLastRow (bool): Whether to copy the value from the last row to the new row.
        emptyRowsText (str | None): Text to display when there are no rows if `hideColumnsIfEmpty` is True.
        hideColumnsIfEmpty (bool): Whether to hide columns if there are no rows.
        maxRowCount (int): Maximum number of rows.
        minRowCount (int): Minimum number of rows.
        removeRowText (str | None): Text for the 'Remove row' button.
        rowCount (int): The initial number of rows.
    """

    addRowLocation: str = "default"
    addRowText: str | None = None
    allowAddRows: bool = True
    allowRemoveRows: bool = True
    allowRowsDragAndDrop: bool = False
    confirmDelete: bool = False
    confirmDeleteText: str | None = None
    defaultRowValue: str | None = None
    defaultValueFromLastRow: bool = False
    emptyRowsText: str | None = None
    hideColumnsIfEmpty: bool = False
    maxRowCount: int = 1000
    minRowCount: int = 0
    removeRowText: str | None = None
    rowCount: int = 2
    type: str = Field(default="matrixdynamic")


class QuestionMultipleTextModel(QuestionModel):
    """A multiple text type question object model"""

    type: str = Field(default="multipletext")

    # TODO


class QuestionNoUiSliderModel(QuestionModel):
    """A noUiSlider type question object model

    Attributes:
        step (int): The step of the slider.
        rangeMin (int): The minimum value of the slider.
        rangeMax (int): The maximum value of the slider.
        pipsMode (str): The mode of the pips. Can be 'positions', 'values', 'count', 'range', 'steps'. See <https://refreshless.com/nouislider/pips/>
        pipsValues (list): The values of the pips.
        pipsText (list): The text of the pips.
        pipsDensity (int): The density of the pips.
        orientation (str): The orientation of the slider. Can be 'horizontal', 'vertical'.
        direction (str): The direction of the slider. Can be 'ltr', 'rtl'.
        tooltips (bool): Whether to show tooltips.
    """

    step: int = 1
    rangeMin: int = 0
    rangeMax: int = 100
    pipsMode: str = "positions"
    pipsValues: list = [0, 25, 50, 75, 100]
    pipsText: list = [0, 25, 50, 75, 100]
    pipsDensity: int = 5
    orientation: str = "horizontal"
    direction: str = "ltr"
    tooltips: bool = True
    type: str = Field(default="nouislider")


class PanelModel(BaseModel):
    """Object model for panel data

    Attributes:
        name (str): The label of the panel.
        questions (QuestionModel | list): The questions on the panel.
        description (str | None): Optional subtitle or description of the panel.
        enableIf (str | None): Expression to enable the panel.
        id (str | None): HTML id attribute for the panel. Usually not necessary.
        innerIndent (int | None): The inner indent of the panel from the left edge. Can be integers from 0 up.
        isRequired (bool): Whether the panel is required (at least one question must be answered).
        maxWidth (str): Maximum width of the panel in CSS units.
        minWidth (str): Minimum width of the panel in CSS units.
        questionErrorLocation (str): The location of the error text for the questions. Can be 'default', 'top', 'bottom'.
        questionsOrder (str): The order of the questions. Can be 'default', 'random', 'initial'.
        questionStartIndex (str | None): The start index of the questions' numbers. Can include prefixes and suffixes. Default is '1.'.
        questionTitleLocation (str): The location of the title for the questions. Can be 'default', 'top', 'bottom'.
        questionTitleWidth (str | None): The width of the question title in CSS units. Only if `questionTitleLocation='left'`.
        readOnly (bool): Whether the panel is read-only.
        requiredErrorText (str | None): Error text if the required condition is not met.
        requiredIf (str | None): Expression to make the panel required.
        rightIndent (int | None): The right indent of the panel from the right edge. Can be integers from 0 up.
        showNumber (bool): Whether to show the panel number.
        showQuestionNumbers (str): Whether to show the question numbers. Can be 'default', 'onpanel', 'off'.
        startWithNewLine (bool): Whether to start the panel on a new line.
        title (str): The visible title of the panel.
        visible (bool): Whether the panel is visible.
        visibleIf (str | None): Expression to make the panel visible.
        width (str): Width of the panel in CSS units.
    """

    name: str
    questions: QuestionModel | list
    description: str | None = None
    enableIf: str | None = None
    id: str | None = None
    innerIndent: int | None = None
    isRequired: bool = False
    maxWidth: str = "100%"
    minWidth: str = "300px"
    questionErrorLocation: str = "default"
    questionsOrder: str = "default"
    questionStartIndex: str | None = None
    questionTitleLocation: str = "default"
    questionTitleWidth: str | None = None
    readOnly: bool = False
    requiredErrorText: str | None = None
    requiredIf: str | None = None
    rightIndent: int | None = None
    showNumber: bool = False
    showQuestionNumbers: str = "default"
    startWithNewLine: bool = True
    title: str | None = None
    visible: bool = True
    visibleIf: str | None = None
    width: str = ""

    def dict(self) -> dict:
        return dict_without_defaults(self) | {
            "type": "panel",
            "elements": [question.dict() for question in self.questions],
        }

    def __iter__(self):
        return iter(self.questions)


class PageModel(BaseModel):
    """Object model for page data

    Attributes:
        name (str): The label of the page.
        questions (QuestionModel | list[QuestionModel]): The questions on the page.
        description (str | None): Optional subtitle or description of the page.
        enableIf (str | None): Expression to enable the page.
        id (str | None): HTML id attribute for the page. Usually not necessary.
        isRequired (bool): Whether the page is required (at least one question must be answered).
        maxTimeToFinish (int | None): Maximum time in seconds to finish the page.
        maxWidth (str): Maximum width of the page in CSS units.
        minWidth (str): Minimum width of the page in CSS units.
        navigationButtonsVisibility (str): The visibility of the navigation buttons. Can be 'inherit', 'show', 'hide'.
        navigationDescription (str | None): Description for the page navigation.
        navigationTitle (str | None): Title for the page navigation.
        questionErrorLocation (str): The location of the error text for the questions. Can be 'default', 'top', 'bottom'.
        questionTitleLocation (str): The location of the title for the questions. Can be 'default', 'top', 'bottom'.
        questionsOrder (str): The order of the questions. Can be 'default', 'random'.
        readOnly (bool): Whether the page is read-only.
        requiredErrorText (str | None): Error text if the required condition is not met.
        requiredIf (str | None): Expression to make the page required (at least one question must be answered).
        state (str): If the page should be collapsed or expanded. Can be 'default', 'collapsed', 'expanded'.
        title (str): The visible title of the page.
        visible (bool): Whether the page is visible.
        visibleIf (str | None): Expression to make the page visible.
        visibleIndex (int | None): The index at which the page should be visible.
        width (str): Width of the page
        addCode (dict | None): Additional code for the page. Usually not necessary.
        customCode (str | None): Custom JS commands to be added to the survey.
        customFunctions (str | None): Custom JS functions definitions to be added to the survey. To be used with `customCode`.
    """

    name: str
    questions: QuestionModel | list
    description: str | None = None
    enableIf: str | None = None
    id: str | None = None
    isRequired: bool = False
    maxTimeToFinish: int | None = None
    maxWidth: str = "100%"
    minWidth: str = "300px"
    navigationButtonsVisibility: str = "inherit"
    navigationDescription: str | None = None
    navigationTitle: str | None = None
    questionErrorLocation: str = "default"
    questionTitleLocation: str = "default"
    questionsOrder: str = "default"
    readOnly: bool = False
    requiredErrorText: str | None = None
    requiredIf: str | None = None
    state: str = "default"
    title: str | None = None
    visible: bool = True
    visibleIf: str | None = None
    visibleIndex: int | None = None
    addCode: dict | None = None
    customCode: str | None = None
    customFunctions: str | None = None

    def __str__(self) -> str:
        return f"Page: {self.name}\n" + "\n".join(
            [str(question) for question in self.questions]
        )

    def dict(self) -> dict:
        return dict_without_defaults(self) | {
            "elements": [question.dict() for question in self.questions]
        }

    def __iter__(self):
        return iter(self.questions)


class SurveyModel(BaseModel):
    """Object model for survey data

    Attributes:
        pages (list[PageModel]): The pages of the survey.
        addScoreToResults (bool): Whether to add the scores of the questions with `correctAnswer` to the results data. See `scoresSuffix`.
        allowCompleteSurveyAutomatic (bool): Whether the survey should complete automatically after all questions on the last page had been answered. Works only if `goNextPageAutomatic=True`. Default is True.
        allowResizeComment (bool): Whether to allow resizing the long questions input area. Default is True. Can be overridden for individual questions.
        autoGrowComment (bool): Whether to automatically grow the long questions input area. Default is False. Can be overridden for individual questions.
        backgroundImage (str | None): URL or base64 of the background image.
        backgroundOpacity (int): The opacity of the background image. 0 is transparent, 1 is opaque.
        calculatedValues (list[dict] | None): The calculated values for the survey. List of dictionaries with keys `name`, `expression` and optionally `includeIntoResult` (bool) to save the value in the db.
        checkErrorsMode (str): The mode of checking errors. Can be 'onNextPage', 'onValueChanged', 'onComplete'.
        commentAreaRows (int): The number of rows for the comment area of the questions with `showCommentArea` or `showOtherItem` set to True. Default is 2. Can be overridden for individual questions.
        completedBeforeHtml (str | None): HTML content to show if the survey had been completed before. Use with `cookieName`.
        completedHtml (str | None): HTML content to show after the survey is completed.
        completedHtmlOnCondition (list[dict] | None): HTML content to show after the survey is completed if the condition is met. List of dictionaries with keys `expression` and `html` keys.
        completeText (str | None): Text for the 'Complete' button.
        cookieName (str | None): The name of the cookie to store the information about the survey having been completed. See `completedBeforeHtml`.
        editText (str | None): Text for the 'Edit' button if `showPreviewBeforeComplete=True`.
        firstPageIsStarted (bool | None): Whether the first page is a start page. Default is False.
        focusFirstQuestionAutomatic (bool): Whether to focus the first question automatically. Default is False.
        focusOnFirstError (bool): Whether to focus on the first error if it was raised. Default is True.
        goNextPageAutomatic (bool): Whether to go to the next page automatically after all questions had been answered. Default is False.
        locale (str): The locale of the survey. Default is 'en'.
        logo (str | None): URL or base64 of the logo image.
        logoFit (str): The `object-fit` CSS property logo image. Can be 'contain', 'cover', 'fill', 'none'.
        logoHeight (str): The height of the logo image in CSS units. Default is '200px'.
        logoPosition (str): The position of the logo image. Can be 'left', 'right', 'none'.
        logoWidth (str): The width of the logo image in CSS units. Default is '300px'.
        matrixDragHandleArea (str): The part of an item with which the users can drag and drop in dynamic matrix questions. Can be 'entireItem' (default), 'icon' (drag icon only).
        maxOthersLength (int): The maximum length of the comment area in the questions with `showOtherItem` or `showCommentArea` set to True. Default is 0 (no limit).
        maxTextLength (int): The maximum length of the text in the textual questions. Default is 0 (no limit).
        maxTimeToFinish (int | None): Maximum time in seconds to finish the survey.
        maxTimeToFinishPage (int | None): Maximum time in seconds to finish the page. 0 means no limit.
        mode (str): The mode of the survey. Can be 'edit' (can be filled), 'display' (read-only).
        navigateToUrl (str | None): URL to navigate to after the survey is completed.
        navigateToUrlOnCondition (list[dict] | None): URL to navigate to after the survey is completed if the condition is met. List of dictionaries with keys `expression` and `url` keys.
        numberOfGroups (int): The number of groups in the survey. Default is 1.
        pageNextText (str | None): Text for the 'Next' button.
        pagePrevText (str | None): Text for the 'Previous' button.
        previewText (str | None): Text for the 'Preview' button if `showPreviewBeforeComplete=True`.
        progressBarInheritWidthFrom (str): The element from which the progress bar should inherit the width. Can be 'container', 'survey'.
        progressBarShowPageNumbers (bool): Whether to show the page numbers on the progress bar. Only if `progressBarType="pages"`. Default is False. See `showProgressBar`.
        progressBarShowPageTitles (bool): Whether to show the page titles on the progress bar. Only if `progressBarType="pages"`. Default is False. See `showProgressBar`.
        progressBarType (str): The type of the progress bar. Can be 'pages' (default), 'questions', 'requiredQuestions', 'correctQuestions'.
        questionDescriptionLocation (str): The location of the description for the questions. Can be 'underTitle' (default), 'underInput'. Can be overridden for individual questions.
        questionErrorLocation (str): The location of the error text for the questions. Can be 'top' (default), 'bottom'. Can be overridden for individual questions.
        questionsOnPageMode (str): The mode of the questions on the page. Can be 'standard' (default; use structure in JSON), 'singlePage' (combine all questions into a single page), 'questionPerPage' (move all questions to separate pages).
        questionsOrder (str): The order of the questions. Can be 'initial' (default), 'random'. Can be overridden for individual pages.
        questionStartIndex (int | str | None): The number or letter with which the questions numbering should start.
        questionTitleLocation (str): The location of the title for the questions. Can be 'top' (default), 'bottom', 'left'. Can be overridden for individual questions or pages.
        questionTitlePattern (str): The pattern of the question title. See <https://surveyjs.io/form-library/documentation/design-survey/configure-question-titles#title-pattern>.
        requiredText (str): The text denoting the required questions. Default is '*'.
        scoresSuffix (str): The suffix of the score column if `addScoreToResults=True`. Default is '_score'.
        showCompletedPage (bool): Whether to show the completed page. Default is True.
        showNavigationButtons (str): The location of the navigation buttons. Can be 'bottom' (default), 'top', 'both', 'none'.
        showPageNumbers (bool | None): Whether to show the page numbers in the pages' titles.
        showPageTitles (bool): Whether to show the page titles. Default is True.
        showPrevButton (bool): Whether to show the 'Previous' button. Default is True.
        showPreviewBeforeComplete (str): Whether to preview all answers before completion. Can be 'noPreview' (default), 'showAllQuestions', 'showAnsweredQuestions'.
        showProgressBar (str): Whether to show the progress bar. Can be 'off' (default), 'aboveHeader', 'belowHeader', 'bottom', 'topBottom', 'auto'.
        showQuestionNumbers (bool | str): Whether to show the question numbers. Default is True. Can be True, 'on', False, 'off', 'onpage' (number each page anew).
        showTimerPanel (str): Whether to show the timer panel. Can be 'none' (default), 'top', 'bottom'. See `maxTimeToFinish`, `maxTimeToFinishPage`, and `showTimerPanelMode`.
        showTimerPanelMode (str): What times to show on the timer panel. Can be 'all' (default), 'page', 'survey'. See `showTimerPanel`.
        showTitle (bool): Whether to show the survey title. Default is True.
        showTOC (bool): Whether to show the table of contents. Default is False. See `tocLocation`.
        startSurveyText (str | None): Text for the 'Start' button if `firstPageIsStarted=True`.
        storeOthersAsComment (bool): Whether to store the 'Other' answers in a separate column (True; see `commentSuffix`) or in the question column (False). Default is True.
        textUpdateMode (str): The mode of updating the text. Can be 'onBlur' (default; update after the field had been unclicked), 'onTyping' (update every key press). Can be overridden for individual questions.
        title (str | None): The title of the survey.
        tocLocation (str): The location of the table of contents. Can be 'left' (default), 'right'. See `showTOC`.
        triggers (str | None): Triggers for the survey. Usually not necessary. See <https://surveyjs.io/form-library/documentation/design-survey/conditional-logic#conditional-survey-logic-triggers>.
        validateVisitedEmptyFields (bool): Whether to validate empty fields that had been clicked, and unclicked empty. Default is False.
        width (str | None): Width of the survey in CSS units. Default is None (inherit from the container).
        widthMode (str): The mode of the width. Can be 'auto' (default; the width is set by the content), 'static', 'responsive'.
        addCode (dict | None): Additional code for the survey. Usually not necessary.
        customCode (str | None): Custom JS commands to be added to the survey.
        customFunctions (str | None): Custom JS functions definitions to be added to the survey. To be used with `customCode`.
    """

    pages: list[PageModel]
    addScoreToResults: bool = True
    allowCompleteSurveyAutomatic: bool = True
    allowResizeComment: bool = True
    autoGrowComment: bool = False
    backgroundImage: str | None = None
    backgroundOpacity: int = 1
    calculatedValues: list[dict] | None = None
    checkErrorsMode: str = "onNextPage"
    commentAreaRows: int = 2
    completedBeforeHtml: str | None = None
    completedHtml: str | None = None
    completedHtmlOnCondition: list[dict] | None = None
    completeText: str | None = None
    cookieName: str | None = None
    editText: str | None = None
    firstPageIsStarted: bool | None = None
    focusFirstQuestionAutomatic: bool = False
    focusOnFirstError: bool = True
    goNextPageAutomatic: bool = False
    locale: str = "en"
    logo: str | None = None
    logoFit: str = "contain"
    logoHeight: str = "200px"
    logoPosition: str = "left"
    logoWidth: str = "300px"
    matrixDragHandleArea: str = "entireItem"
    maxOthersLength: int = 0
    maxTextLength: int = 0
    maxTimeToFinish: int | None = None
    maxTimeToFinishPage: int | None = None
    mode: str = "edit"
    navigateToUrl: str | None = None
    navigateToUrlOnCondition: list[dict] | None = None
    numberOfGroups: int = 1
    pageNextText: str | None = None
    pagePrevText: str | None = None
    previewText: str | None = None
    progressBarInheritWidthFrom: str = "container"
    progressBarShowPageNumbers: bool = False
    progressBarShowPageTitles: bool = False
    progressBarType: str = "pages"
    questionDescriptionLocation: str = "underTitle"
    questionErrorLocation: str = "top"
    questionsOnPageMode: str = "standard"
    questionsOrder: str = "initial"
    questionStartIndex: int | str | None = None
    questionTitleLocation: str = "top"
    questionTitlePattern: str = "numTitleRequire"
    requiredText: str = "*"
    scoresSuffix: str = "_score"
    showCompletedPage: bool = True
    showNavigationButtons: str = "bottom"
    showPageNumbers: bool | None = None
    showPageTitles: bool = True
    showPrevButton: bool = True
    showPreviewBeforeComplete: str = "noPreview"
    showProgressBar: str = "off"
    showQuestionNumbers: bool | str = True
    showTimerPanel: str = "none"
    showTimerPanelMode: str = "all"
    showTitle: bool = True
    showTOC: bool = False
    startSurveyText: str | None = None
    storeOthersAsComment: bool = True
    textUpdateMode: str = "onBlur"
    title: str | None = None
    tocLocation: str = "left"
    triggers: list[dict] | None = None
    validateVisitedEmptyFields: bool = False
    width: str | None = None
    widthMode: str = "auto"
    addCode: dict | None = None
    customCode: str | None = None
    customFunctions: str | None = None

    def __str__(self) -> str:
        first_line = "VelesSurvey" + (f' ("{self.title}")\n' if self.title else "\n")
        return (
            first_line
            + "-" * (len(first_line) - 1)
            + "\n"
            + "\n".join([str(page) for page in self.pages])
            + "-" * (len(first_line) - 1)
        )

    def __iter__(self):
        return iter(self.pages)

    def dict(self) -> dict:
        return dict_without_defaults(self) | {
            "pages": [page.dict() for page in self.pages]
        }

    def json(self) -> str:
        return json.dumps(self.dict())

    def extractKey(self, keyName) -> str:
        "Extracts the data with a specified key from self.dict()"
        # Retrieve the dictionary data.
        data = self.dict()

        # Initialize an empty list to store customCode values.
        result = []
        # Create a stack with the initial data to iterate through.
        stack = [data]

        # Loop through the stack until it's empty.
        while stack:
            current = stack.pop()

            # If current item is a dictionary, process its keys and values.
            if isinstance(current, dict):
                for key, value in current.items():
                    # If the key is 'customCode', add its value to the result list.
                    if key == keyName:
                        result.append(value)
                    # Add the value to the stack for further processing.
                    stack.append(value)

            # If current item is a list, add all its elements to the stack.
            elif isinstance(current, list):
                stack.extend(current)
        if len(result) == 0 or (len(result) == 1 and result[0] == ""):
            return r"// placeholder"
        return "\n\n".join([f"  {result}" for result in result])

    def build(self, path: str | Path = os.getcwd(), folderName: str = "survey"):
        """Create the file structure for the survey but not build it"""

        if isinstance(path, str):
            path = Path(path)

        path = path / folderName

        # main file structure
        if not os.path.exists(path / "package.json"):
            template = str(files("velesresearch.website_template"))
            if "node_modules" in template:
                template.remove("node_modules")
            shutil.copytree(
                template,
                path,
                ignore=shutil.ignore_patterns("__pycache__", "__init__.py"),
            )

        # do bun stuff if needed
        if not os.path.exists(path / "node_modules"):
            subprocess.run("bun install", cwd=path, shell=True, check=False)

        # survey.js
        with open(path / "src" / "survey.js", "w", encoding="utf-8") as survey_js:
            survey_js.write("export const json = " + self.json() + ";")

        # config.ts
        shutil.copyfile(
            files("velesresearch.website_template") / "src" / "config.ts",
            path / "src" / "config.ts",
        )
        with open(path / "src" / "config.ts", "r", encoding="utf-8") as configTS:
            configTSData = configTS.read()

            # number of groups
            configTSData = configTSData.replace(
                r"{% numberOfGroups %}", str(self.numberOfGroups)
            )
        with open(path / "src" / "config.ts", "w", encoding="utf-8") as configTS:
            configTS.write(configTSData)

        # customCode
        with open(path / "src" / "SurveyComponent.jsx", "r", encoding="UTF-8") as file:
            surveyComponentData = file.read()

        surveyComponentData = re.sub(
            r"(?<=  \/\/ \{% customCode %\}\n\n).+(?=\n\n  \/\/ \{% end customCode %\})",
            self.extractKey("customCode"),
            surveyComponentData,
            flags=re.M | re.S,
        )
        surveyComponentData = re.sub(
            r"(?<=\/\/ \{% customFunctions %\}\n\n).+(?=\n\n\/\/ \{% end customFunctions %\})",
            self.extractKey("customFunctions"),
            surveyComponentData,
            flags=re.M | re.S,
        )

        with open(path / "src" / "SurveyComponent.jsx", "w", encoding="UTF-8") as file:
            file.write(surveyComponentData)

        subprocess.run("bun run build", cwd=path, shell=True, check=False)
