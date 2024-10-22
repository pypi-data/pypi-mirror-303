"""Functions creating objects for survey structure classes"""

from .models import *
from .helperModels import ValidatorModel
from .utils import flatten
from .validators import expressionValidator


def survey(
    *pages: PageModel | list[PageModel],
    build: bool = True,
    folderName: str = "survey",
    path: str | Path = os.getcwd(),
    addScoreToResults: bool = True,
    allowCompleteSurveyAutomatic: bool = True,
    allowResizeComment: bool = True,
    autoGrowComment: bool = False,
    backgroundImage: str | None = None,
    backgroundOpacity: int = 1,
    calculatedValues: list[dict] | None = None,
    checkErrorsMode: str = "onNextPage",
    commentAreaRows: int = 2,
    completedBeforeHtml: str | None = None,
    completedHtml: str | None = None,
    completedHtmlOnCondition: list[dict] | None = None,
    completeText: str | None = None,
    cookieName: str | None = None,
    editText: str | None = None,
    firstPageIsStarted: bool | None = None,
    focusFirstQuestionAutomatic: bool = False,
    focusOnFirstError: bool = True,
    goNextPageAutomatic: bool = False,
    locale: str = "en",
    logo: str | None = None,
    logoFit: str = "contain",
    logoHeight: str = "200px",
    logoPosition: str = "left",
    logoWidth: str = "300px",
    matrixDragHandleArea: str = "entireItem",
    maxOthersLength: int = 0,
    maxTextLength: int = 0,
    maxTimeToFinish: int | None = None,
    maxTimeToFinishPage: int | None = None,
    mode: str = "edit",
    navigateToUrl: str | None = None,
    navigateToUrlOnCondition: list[dict] | None = None,
    numberOfGroups: int = 1,
    pageNextText: str | None = None,
    pagePrevText: str | None = None,
    previewText: str | None = None,
    progressBarInheritWidthFrom: str = "container",
    progressBarShowPageNumbers: bool = False,
    progressBarShowPageTitles: bool = False,
    progressBarType: str = "pages",
    questionDescriptionLocation: str = "underTitle",
    questionErrorLocation: str = "top",
    questionsOnPageMode: str = "standard",
    questionsOrder: str = "initial",
    questionStartIndex: int | str | None = None,
    questionTitleLocation: str = "top",
    questionTitlePattern: str = "numTitleRequire",
    requiredText: str = "*",
    scoresSuffix: str = "_score",
    showCompletedPage: bool = True,
    showNavigationButtons: str = "bottom",
    showPageNumbers: bool | None = None,
    showPageTitles: bool = True,
    showPrevButton: bool = True,
    showPreviewBeforeComplete: str = "noPreview",
    showProgressBar: str = "off",
    showQuestionNumbers: bool | str = True,
    showTimerPanel: str = "none",
    showTimerPanelMode: str = "all",
    showTitle: bool = True,
    showTOC: bool = False,
    startSurveyText: str | None = None,
    storeOthersAsComment: bool = True,
    textUpdateMode: str = "onBlur",
    title: str | None = None,
    tocLocation: str = "left",
    triggers: list[dict] | None = None,
    validateVisitedEmptyFields: bool = False,
    width: str | None = None,
    widthMode: str = "auto",
    addCode: dict | None = None,
    **kwargs,
) -> SurveyModel:
    """Create a survey object

    Args:
        pages (list[PageModel]): The pages of the survey.
        build (bool): Whether to build the survey. Default is True.
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
    args = {
        "addScoreToResults": addScoreToResults,
        "allowCompleteSurveyAutomatic": allowCompleteSurveyAutomatic,
        "allowResizeComment": allowResizeComment,
        "autoGrowComment": autoGrowComment,
        "backgroundImage": backgroundImage,
        "backgroundOpacity": backgroundOpacity,
        "calculatedValues": calculatedValues,
        "checkErrorsMode": checkErrorsMode,
        "commentAreaRows": commentAreaRows,
        "completedBeforeHtml": completedBeforeHtml,
        "completedHtml": completedHtml,
        "completedHtmlOnCondition": completedHtmlOnCondition,
        "completeText": completeText,
        "cookieName": cookieName,
        "editText": editText,
        "firstPageIsStarted": firstPageIsStarted,
        "focusFirstQuestionAutomatic": focusFirstQuestionAutomatic,
        "focusOnFirstError": focusOnFirstError,
        "goNextPageAutomatic": goNextPageAutomatic,
        "locale": locale,
        "logo": logo,
        "logoFit": logoFit,
        "logoHeight": logoHeight,
        "logoPosition": logoPosition,
        "logoWidth": logoWidth,
        "matrixDragHandleArea": matrixDragHandleArea,
        "maxOthersLength": maxOthersLength,
        "maxTextLength": maxTextLength,
        "maxTimeToFinish": maxTimeToFinish,
        "maxTimeToFinishPage": maxTimeToFinishPage,
        "mode": mode,
        "navigateToUrl": navigateToUrl,
        "navigateToUrlOnCondition": navigateToUrlOnCondition,
        "numberOfGroups": numberOfGroups,
        "pageNextText": pageNextText,
        "pagePrevText": pagePrevText,
        "previewText": previewText,
        "progressBarInheritWidthFrom": progressBarInheritWidthFrom,
        "progressBarShowPageNumbers": progressBarShowPageNumbers,
        "progressBarShowPageTitles": progressBarShowPageTitles,
        "progressBarType": progressBarType,
        "questionDescriptionLocation": questionDescriptionLocation,
        "questionErrorLocation": questionErrorLocation,
        "questionsOnPageMode": questionsOnPageMode,
        "questionsOrder": questionsOrder,
        "questionStartIndex": questionStartIndex,
        "questionTitleLocation": questionTitleLocation,
        "questionTitlePattern": questionTitlePattern,
        "requiredText": requiredText,
        "scoresSuffix": scoresSuffix,
        "showCompletedPage": showCompletedPage,
        "showNavigationButtons": showNavigationButtons,
        "showPageNumbers": showPageNumbers,
        "showPageTitles": showPageTitles,
        "showPrevButton": showPrevButton,
        "showPreviewBeforeComplete": showPreviewBeforeComplete,
        "showProgressBar": showProgressBar,
        "showQuestionNumbers": showQuestionNumbers,
        "showTimerPanel": showTimerPanel,
        "showTimerPanelMode": showTimerPanelMode,
        "showTitle": showTitle,
        "showTOC": showTOC,
        "startSurveyText": startSurveyText,
        "storeOthersAsComment": storeOthersAsComment,
        "textUpdateMode": textUpdateMode,
        "title": title,
        "tocLocation": tocLocation,
        "triggers": triggers,
        "validateVisitedEmptyFields": validateVisitedEmptyFields,
        "width": width,
        "widthMode": widthMode,
        "addCode": addCode,
    }
    pages = flatten(pages)
    surveyObject = SurveyModel(pages=pages, **args, **kwargs)
    if build:
        surveyObject.build(path=path, folderName=folderName)
    return surveyObject


def page(
    name: str,
    *questions: QuestionModel | list[QuestionModel],
    description: str | None = None,
    enableIf: str | None = None,
    id: str | None = None,
    isRequired: bool = False,
    maxTimeToFinish: int | None = None,
    maxWidth: str = "100%",
    minWidth: str = "300px",
    navigationButtonsVisibility: str = "inherit",
    navigationDescription: str | None = None,
    navigationTitle: str | None = None,
    questionErrorLocation: str = "default",
    questionTitleLocation: str = "default",
    questionsOrder: str = "default",
    readOnly: bool = False,
    requiredErrorText: str | None = None,
    requiredIf: str | None = None,
    state: str = "default",
    title: str | None = None,
    visible: bool = True,
    visibleIf: str | None = None,
    visibleIndex: int | None = None,
    addCode: dict | None = None,
    **kwargs,
) -> PageModel:
    """Create a page object

    Args:
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
        addCode (dict | None): Additional code for the survey. Usually not necessary.
        customCode (str | None): Custom JS commands to be added to the survey.
        customFunctions (str | None): Custom JS functions definitions to be added to the survey. To be used with `customCode`.
    """
    args = {
        "description": description,
        "enableIf": enableIf,
        "id": id,
        "isRequired": isRequired,
        "maxTimeToFinish": maxTimeToFinish,
        "maxWidth": maxWidth,
        "minWidth": minWidth,
        "navigationButtonsVisibility": navigationButtonsVisibility,
        "navigationDescription": navigationDescription,
        "navigationTitle": navigationTitle,
        "questionErrorLocation": questionErrorLocation,
        "questionTitleLocation": questionTitleLocation,
        "questionsOrder": questionsOrder,
        "readOnly": readOnly,
        "requiredErrorText": requiredErrorText,
        "requiredIf": requiredIf,
        "state": state,
        "title": title,
        "visible": visible,
        "visibleIf": visibleIf,
        "visibleIndex": visibleIndex,
        "addCode": addCode,
    }
    questions = flatten(questions)
    return PageModel(
        name=name,
        questions=questions,
        **args,
        **kwargs,
    )


def panel(
    name: str,
    *questions: QuestionModel | list[QuestionModel],
    description: str | None = None,
    enableIf: str | None = None,
    id: str | None = None,
    innerIndent: int | None = None,
    isRequired: bool = False,
    maxWidth: str = "100%",
    minWidth: str = "300px",
    questionErrorLocation: str = "default",
    questionsOrder: str = "default",
    questionStartIndex: str | None = None,
    questionTitleLocation: str = "default",
    questionTitleWidth: str | None = None,
    readOnly: bool = False,
    requiredErrorText: str | None = None,
    requiredIf: str | None = None,
    rightIndent: int | None = None,
    showNumber: bool = False,
    showQuestionNumbers: str = "default",
    startWithNewLine: bool = True,
    visible: bool = True,
    visibleIf: str | None = None,
    width: str = "",
    **kwargs,
) -> PanelModel:
    """
    Create a panel.

    Args:
        name (str): The label of the page.
        questions (QuestionModel | list[QuestionModel]): The questions on the panel.
        description (str | None): Optional subtitle or description of the panel.
        enableIf (str | None): Expression to enable the panel.
        id (str | None): HTML id attribute for the panel. Usually not necessary.
        innerIndent (int | None): The inner indent of the panel.
        isRequired (bool): Whether the panel is required (at least one question must be answered).
        maxWidth (str): Maximum width of the panel in CSS units.
        minWidth (str): Minimum width of the panel in CSS units.
        questionErrorLocation (str): The location of the error text for the questions. Can be 'default', 'top', 'bottom'.
        questionsOrder (str): The order of the questions. Can be 'default', 'random'.
        questionStartIndex (str | None): The number or letter with which the questions numbering should start.
        questionTitleLocation (str): The location of the title for the questions. Can be 'default', 'top', 'bottom'.
        questionTitleWidth (str | None): The width of the question title.
        readOnly (bool): Whether the panel is read-only.
        requiredErrorText (str | None): Error text if the required condition is not met.
        requiredIf (str | None): Expression to make the panel required (at least one question must be answered).
        rightIndent (int | None): The right indent of the panel.
        showNumber (bool): Whether to show the panel number.
        showQuestionNumbers (str): Whether to show the question numbers. Can be 'default', 'on', 'off', 'onpage' (number each page anew).
        startWithNewLine (bool): Whether to start the panel on a new line.
        visible (bool): Whether the panel is visible.
        visibleIf (str | None): Expression to make the panel visible.
        width (str): Width of the panel.
    """
    args = {
        "description": description,
        "enableIf": enableIf,
        "id": id,
        "innerIndent": innerIndent,
        "isRequired": isRequired,
        "maxWidth": maxWidth,
        "minWidth": minWidth,
        "questionErrorLocation": questionErrorLocation,
        "questionsOrder": questionsOrder,
        "questionStartIndex": questionStartIndex,
        "questionTitleLocation": questionTitleLocation,
        "questionTitleWidth": questionTitleWidth,
        "readOnly": readOnly,
        "requiredErrorText": requiredErrorText,
        "requiredIf": requiredIf,
        "rightIndent": rightIndent,
        "showNumber": showNumber,
        "showQuestionNumbers": showQuestionNumbers,
        "startWithNewLine": startWithNewLine,
        "visible": visible,
        "visibleIf": visibleIf,
        "width": width,
    }
    questions = flatten(questions)
    return PanelModel(
        name=name,
        questions=questions,
        **args,
        **kwargs,
    )


def dropdown(
    name: str,
    title: str | list[str] | None,
    *choices: str | dict | list,
    titleLocation: str = "default",
    description: str | None = None,
    descriptionLocation: str = "default",
    isRequired: bool = False,
    readOnly: bool = False,
    visible: bool = True,
    requiredIf: str | None = None,
    enableIf: str | None = None,
    visibleIf: str | None = None,
    validators: ValidatorModel | list[ValidatorModel] | None = None,
    showOtherItem: bool = False,
    showCommentArea: bool = False,
    commentPlaceholder: str | None = None,
    commentText: str | None = None,
    correctAnswer: str | None = None,
    defaultValue: str | None = None,
    defaultValueExpression: str | None = None,
    requiredErrorText: str | None = None,
    errorLocation: str = "default",
    hideNumber: bool = False,
    id: str | None = None,
    maxWidth: str = "100%",
    minWidth: str = "300px",
    resetValueIf: str | None = None,
    setValueIf: str | None = None,
    setValueExpression: str | None = None,
    startWithNewLine: bool = True,
    state: str = "default",
    useDisplayValuesInDynamicTexts: bool = True,
    width: str = "",
    addCode: dict | None = None,
    choicesFromQuestion: str | None = None,
    choicesFromQuestionMode: str = "all",
    choicesOrder: str = "none",
    showDontKnowItem: bool = False,
    dontKnowText: str | None = None,
    hideIfChoicesEmpty: bool | None = None,
    showNoneItem: bool = False,
    noneText: str | None = None,
    otherText: str | None = None,
    otherErrorText: str | None = None,
    showRefuseItem: bool = False,
    refuseText: str | None = None,
    choicesMax: int | None = None,
    choicesMin: int | None = None,
    choicesStep: int | None = None,
    placeholder: str | None = None,
    **kwargs,
) -> QuestionDropdownModel | list[QuestionDropdownModel]:
    """Create a single-select dropdown question object

    Args:
        name (str): The label of the question.
        title (str | None): The visible title of the question. If None, `name` is used.
        choices (str | dict | list): The choices for the question. Can be string(s) or dictionary(-ies) with structure `{"value": ..., "text": ...}`. You can also add `visibleIf`, `enableIf`, and `requiredIf` to the dictionary.
        choicesFromQuestion (str | None): The name of the question to get the choices from if the are to be copied. Use with `choicesFromQuestionMode`.
        choicesFromQuestionMode (str): The mode of copying choices. Can be 'all', 'selected', 'unselected'.
        choicesMax (int | None): Maximum for automatically generated choices. Use with `choicesMin` and `choicesStep`.
        choicesMin (int | None): Minimum for automatically generated choices. Use with `choicesMax` and `choicesStep`.
        choicesOrder (str): The order of the choices. Can be 'none', 'asc', 'desc', 'random'.
        choicesStep (int | None): Step for automatically generated choices. Use with `choicesMax` and `choicesMin`.
        commentPlaceholder (str | None): Placeholder text for the comment area.
        commentText (str | None): Text for the comment area.
        correctAnswer (str | None): Correct answer for the question. Use for quizzes.
        defaultValue (str | None): Default value for the question.
        defaultValueExpression (str | None): Expression deciding the default value for the question.
        description (str | None): Optional subtitle or description of the question.
        descriptionLocation (str): The location of the description. Can be 'default', 'underTitle', 'underInput'.
        dontKnowText: str | None = None
        enableIf (str | None): Expression to enable the question.
        errorLocation (str | None): Location of the error text. Can be 'default' 'top', 'bottom'.
        hideIfChoicesEmpty: bool | None = None
        hideNumber (bool): Whether to hide the question number.
        id (str | None): HTML id attribute for the question. Usually not necessary.
        maxWidth (str): Maximum width of the question in CSS units.
        minWidth (str): Minimum width of the question in CSS units.
        noneText: str | None = None
        otherErrorText: str | None = None
        otherText: str | None = None
        placeholder (str | None): Placeholder text.
        readOnly (bool): Whether the question is read-only.
        refuseText: str | None = None
        isRequired (bool): Whether the question is required.
        requiredErrorText (str | None): Error text if the required condition is not met.
        requiredIf (str | None): Expression to make the question required.
        resetValueIf (str | None): Expression to reset the value of the question.
        setValueExpression (str | None): Expression to decide on the value of the question to be set. Requires `setValueIf`.
        setValueIf (str | None): Expression with a condition to set the value of the question. Requires `setValueExpression`.
        showCommentArea (bool): Whether to show the comment area. Doesn't work with `showOtherItem`.
        showDontKnowItem: bool = False
        showNoneItem: bool = False
        showOtherItem (bool): Whether to show the 'Other' item. Doesn't work with `showCommentArea`.
        showOtherItem: bool = False
        showRefuseItem: bool = False
        startWithNewLine (bool): Whether to start the question on a new line.
        state (str | None): If the question should be collapsed or expanded. Can be 'default', 'collapsed', 'expanded'.
        titleLocation (str): The location of the title. Can be 'default', 'top', 'bottom', 'left', 'hidden'.
        useDisplayValuesInDynamicTexts (bool): Whether to use display names for question values in placeholders.
        validators (ValidatorModel | list[ValidatorModel] | None): Validator(s) for the question.
        visible (bool): Whether the question is visible.
        visibleIf (str | None): Expression to make the question visible.
        width (str): Width of the question in CSS units.
        addCode (dict | None): Additional code for the question. Usually not necessary.
        customCode (str | None): Custom JS commands to be added to the survey.
        customFunctions (str | None): Custom JS functions definitions to be added to the survey. To be used with `customCode`.
    """
    args = {
        "titleLocation": titleLocation,
        "description": description,
        "descriptionLocation": descriptionLocation,
        "isRequired": isRequired,
        "readOnly": readOnly,
        "visible": visible,
        "requiredIf": requiredIf,
        "enableIf": enableIf,
        "visibleIf": visibleIf,
        "validators": validators,
        "showOtherItem": showOtherItem,
        "showCommentArea": showCommentArea,
        "commentPlaceholder": commentPlaceholder,
        "commentText": commentText,
        "correctAnswer": correctAnswer,
        "defaultValue": defaultValue,
        "defaultValueExpression": defaultValueExpression,
        "requiredErrorText": requiredErrorText,
        "errorLocation": errorLocation,
        "hideNumber": hideNumber,
        "id": id,
        "maxWidth": maxWidth,
        "minWidth": minWidth,
        "resetValueIf": resetValueIf,
        "setValueIf": setValueIf,
        "setValueExpression": setValueExpression,
        "startWithNewLine": startWithNewLine,
        "state": state,
        "useDisplayValuesInDynamicTexts": useDisplayValuesInDynamicTexts,
        "width": width,
        "addCode": addCode,
        "choicesFromQuestion": choicesFromQuestion,
        "choicesFromQuestionMode": choicesFromQuestionMode,
        "choicesOrder": choicesOrder,
        "showDontKnowItem": showDontKnowItem,
        "dontKnowText": dontKnowText,
        "hideIfChoicesEmpty": hideIfChoicesEmpty,
        "showNoneItem": showNoneItem,
        "noneText": noneText,
        "otherText": otherText,
        "otherErrorText": otherErrorText,
        "showRefuseItem": showRefuseItem,
        "refuseText": refuseText,
        "choicesMax": choicesMax,
        "choicesMin": choicesMin,
        "choicesStep": choicesStep,
        "placeholder": placeholder,
    }
    choices = flatten(choices)
    if not isinstance(title, list):
        title = [title]
    if len(title) != 1:
        return [
            QuestionDropdownModel(
                name=f"{name}_{i+1}", title=t, choices=choices, **args, **kwargs
            )
            for i, t in enumerate(title)
        ]
    else:
        return QuestionDropdownModel(
            name=name, title=title[0], choices=choices, **args, **kwargs
        )


def text(
    name: str,
    *title: str | list[str] | None,
    titleLocation: str = "default",
    description: str | None = None,
    descriptionLocation: str = "default",
    isRequired: bool = False,
    readOnly: bool = False,
    visible: bool = True,
    requiredIf: str | None = None,
    enableIf: str | None = None,
    visibleIf: str | None = None,
    validators: ValidatorModel | list[ValidatorModel] | None = None,
    showOtherItem: bool = False,
    showCommentArea: bool = False,
    commentPlaceholder: str | None = None,
    commentText: str | None = None,
    correctAnswer: str | None = None,
    defaultValue: str | None = None,
    defaultValueExpression: str | None = None,
    requiredErrorText: str | None = None,
    errorLocation: str = "default",
    hideNumber: bool = False,
    id: str | None = None,
    maxWidth: str = "100%",
    minWidth: str = "300px",
    resetValueIf: str | None = None,
    setValueIf: str | None = None,
    setValueExpression: str | None = None,
    startWithNewLine: bool = True,
    state: str = "default",
    useDisplayValuesInDynamicTexts: bool = True,
    width: str = "",
    addCode: dict | None = None,
    autocomplete: str | None = None,
    inputType: str = "text",
    max: str | int | None = None,
    maxErrorText: str | None = None,
    maxLength: int | None = None,
    maxValueExpression: str | None = None,
    min: str | int | None = None,
    minErrorText: str | None = None,
    minValueExpression: str | None = None,
    monitorInput: bool = False,
    placeholder: str | None = None,
    size: int | None = None,
    step: str | None = None,
    textUpdateMode: str = "default",
    **kwargs,
) -> QuestionTextModel:
    """Create a text question object

    Args:
        name (str): The label of the question.
        title (str | None): The visible title of the question. If None, `name` is used.
        autocomplete (str | None): A value of `autocomplete` attribute for `<input>`. See MDN for a list: <https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/autocomplete#token_list_tokens>.
        commentPlaceholder (str | None): Placeholder text for the comment area.
        commentText (str | None): Text for the comment area.
        correctAnswer (str | None): Correct answer for the question. Use for quizzes.
        defaultValue (str | None): Default value for the question.
        defaultValueExpression (str | None): Expression deciding the default value for the question.
        description (str | None): Optional subtitle or description of the question.
        descriptionLocation (str): The location of the description. Can be 'default', 'underTitle', 'underInput'.
        enableIf (str | None): Expression to enable the question.
        errorLocation (str | None): Location of the error text. Can be 'default' 'top', 'bottom'.
        hideNumber (bool): Whether to hide the question number.
        id (str | None): HTML id attribute for the question. Usually not necessary.
        inputType (str | None): The type of the input. Can be 'text', 'password', 'email', 'url', 'tel', 'number', 'date', 'datetime-local', 'time', 'month', 'week', 'color'.
        max (str): The `max` attribute of `<input>`. Syntax depends on the `inputType`. See MDN for details: <https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/max>.
        maxErrorText (str | None): Error text if the value exceeds `max`.
        maxLength (int | None): The maximum length of the input in characters. Use 0 for no limit. Use -1 for the default limit.
        maxValueExpression (str | None): Expression to decide the maximum value.
        maxWidth (str): Maximum width of the question in CSS units.
        min (str | None): The `min` attribute of `<input>`. Syntax depends on the `inputType`. See MDN for details: <https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/min>.
        minErrorText (str | None): Error text if the value is less than `min`.
        minValueExpression (str | None): Expression to decide the minimum value.
        minWidth (str): Minimum width of the question in CSS units.
        monitorInput (bool): Whether to count the time spent with the question focused and the number of key presses. Useful for bot detection.
        placeholder (str | None): Placeholder text for the input.
        readOnly (bool): Whether the question is read-only.
        isRequired (bool): Whether the question is required.
        requiredErrorText (str | None): Error text if the required condition is not met.
        requiredIf (str | None): Expression to make the question required.
        resetValueIf (str | None): Expression to reset the value of the question.
        setValueExpression (str | None): Expression to decide on the value of the question to be set. Requires `setValueIf`.
        setValueIf (str | None): Expression with a condition to set the value of the question. Requires `setValueExpression`.
        showCommentArea (bool): Whether to show the comment area. Doesn't work with `showOtherItem`.
        showOtherItem (bool): Whether to show the 'Other' item. Doesn't work with `showCommentArea`.
        size (int | None): The width of the input in characters. A value for `size` attribute of `<input>`.
        startWithNewLine (bool): Whether to start the question on a new line.
        state (str | None): If the question should be collapsed or expanded. Can be 'default', 'collapsed', 'expanded'.
        step (str | None): The `step` attribute of `<input>`. Syntax depends on the `inputType`. See MDN for details: <https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/step>.
        textUpdateMode (str): The mode of updating the text. Can be 'default', 'onBlur' (update after the field had been unclicked), 'onTyping' (update every key press).
        titleLocation (str): The location of the title. Can be 'default', 'top', 'bottom', 'left', 'hidden'.
        useDisplayValuesInDynamicTexts (bool): Whether to use display names for question values in placeholders.
        validators (ValidatorModel | list[ValidatorModel] | None): Validator(s) for the question.
        visible (bool): Whether the question is visible.
        visibleIf (str | None): Expression to make the question visible.
        width (str): Width of the question in CSS units.
        addCode (dict | None): Additional code for the question. Usually not necessary.
        customCode (str | None): Custom JS commands to be added to the survey.
        customFunctions (str | None): Custom JS functions definitions to be added to the survey. To be used with `customCode`.
    """
    args = {
        "titleLocation": titleLocation,
        "description": description,
        "descriptionLocation": descriptionLocation,
        "isRequired": isRequired,
        "readOnly": readOnly,
        "visible": visible,
        "requiredIf": requiredIf,
        "enableIf": enableIf,
        "visibleIf": visibleIf,
        "validators": validators,
        "showOtherItem": showOtherItem,
        "showCommentArea": showCommentArea,
        "commentPlaceholder": commentPlaceholder,
        "commentText": commentText,
        "correctAnswer": correctAnswer,
        "defaultValue": defaultValue,
        "defaultValueExpression": defaultValueExpression,
        "requiredErrorText": requiredErrorText,
        "errorLocation": errorLocation,
        "hideNumber": hideNumber,
        "id": id,
        "maxWidth": maxWidth,
        "minWidth": minWidth,
        "resetValueIf": resetValueIf,
        "setValueIf": setValueIf,
        "setValueExpression": setValueExpression,
        "startWithNewLine": startWithNewLine,
        "state": state,
        "useDisplayValuesInDynamicTexts": useDisplayValuesInDynamicTexts,
        "width": width,
        "addCode": addCode,
        "autocomplete": autocomplete,
        "inputType": inputType,
        "max": max,
        "maxErrorText": maxErrorText,
        "maxLength": maxLength,
        "maxValueExpression": maxValueExpression,
        "min": min,
        "minErrorText": minErrorText,
        "minValueExpression": minValueExpression,
        "monitorInput": monitorInput,
        "placeholder": placeholder,
        "size": size,
        "step": step,
        "textUpdateMode": textUpdateMode,
    }
    title = flatten(title)
    if len(title) != 1:
        return [
            QuestionTextModel(name=f"{name}_{i+1}", title=t, **args, **kwargs)
            for i, t in enumerate(title)
        ]
    return QuestionTextModel(name=name, title=title[0], **args, **kwargs)


def checkbox(
    name: str,
    title: str | list[str] | None,
    *choices: str | dict | list,
    titleLocation: str = "default",
    description: str | None = None,
    descriptionLocation: str = "default",
    isRequired: bool = False,
    readOnly: bool = False,
    visible: bool = True,
    requiredIf: str | None = None,
    enableIf: str | None = None,
    visibleIf: str | None = None,
    validators: ValidatorModel | list[ValidatorModel] | None = None,
    showOtherItem: bool = False,
    showCommentArea: bool = False,
    commentPlaceholder: str | None = None,
    commentText: str | None = None,
    correctAnswer: str | None = None,
    defaultValue: str | None = None,
    defaultValueExpression: str | None = None,
    requiredErrorText: str | None = None,
    errorLocation: str = "default",
    hideNumber: bool = False,
    id: str | None = None,
    maxWidth: str = "100%",
    minWidth: str = "300px",
    resetValueIf: str | None = None,
    setValueIf: str | None = None,
    setValueExpression: str | None = None,
    startWithNewLine: bool = True,
    state: str = "default",
    useDisplayValuesInDynamicTexts: bool = True,
    width: str = "",
    addCode: dict | None = None,
    choicesFromQuestion: str | None = None,
    choicesFromQuestionMode: str = "all",
    choicesOrder: str = "none",
    showDontKnowItem: bool = False,
    dontKnowText: str | None = None,
    hideIfChoicesEmpty: bool | None = None,
    showNoneItem: bool = False,
    noneText: str | None = None,
    otherText: str | None = None,
    otherErrorText: str | None = None,
    showRefuseItem: bool = False,
    refuseText: str | None = None,
    colCount: int | None = None,
    isAllSelected: bool | None = None,
    maxSelectedChoices: int = 0,
    minSelectedChoices: int = 0,
    selectAllText: str | None = None,
    showSelectAllItem: bool | None = None,
    **kwargs,
) -> QuestionCheckboxModel | list[QuestionCheckboxModel]:
    """Create a checkbox question object

    Args:
        name (str): The label of the question.
        title (str | None): The visible title of the question. If None, `name` is used.
        choices (str | dict | list): The choices for the question. Can be string(s) or dictionary(-ies) with structure `{"value": ..., "text": ...}`. You can also add `visibleIf`, `enableIf`, and `requiredIf` to the dictionary.
        choicesFromQuestion (str | None): The name of the question to get the choices from if the are to be copied. Use with `choicesFromQuestionMode`.
        choicesFromQuestionMode (str): The mode of copying choices. Can be 'all', 'selected', 'unselected'.
        choicesOrder (str): The order of the choices. Can be 'none', 'asc', 'desc', 'random'.
        colCount (int | None): The number of columns for the choices. 0 means a single line.
        commentPlaceholder (str | None): Placeholder text for the comment area.
        commentText (str | None): Text for the comment area.
        correctAnswer (str | None): Correct answer for the question. Use for quizzes.
        defaultValue (str | None): Default value for the question.
        defaultValueExpression (str | None): Expression deciding the default value for the question.
        description (str | None): Optional subtitle or description of the question.
        descriptionLocation (str): The location of the description. Can be 'default', 'underTitle', 'underInput'.
        dontKnowText: str | None = None
        enableIf (str | None): Expression to enable the question.
        errorLocation (str | None): Location of the error text. Can be 'default' 'top', 'bottom'.
        hideIfChoicesEmpty: bool | None = None
        hideNumber (bool): Whether to hide the question number.
        id (str | None): HTML id attribute for the question. Usually not necessary.
        isAllSelected (bool | None): Start with all choices selected. Default is False.
        maxSelectedChoices (int): Maximum number of selected choices. 0 means no limit.
        maxWidth (str): Maximum width of the question in CSS units.
        minSelectedChoices (int): Minimum number of selected choices. 0 means no limit.
        minWidth (str): Minimum width of the question in CSS units.
        noneText: str | None = None
        otherErrorText: str | None = None
        otherText: str | None = None
        readOnly (bool): Whether the question is read-only.
        refuseText: str | None = None
        isRequired (bool): Whether the question is required.
        requiredErrorText (str | None): Error text if the required condition is not met.
        requiredIf (str | None): Expression to make the question required.
        resetValueIf (str | None): Expression to reset the value of the question.
        selectAllText (str | None): Text for the 'Select All' item.
        setValueExpression (str | None): Expression to decide on the value of the question to be set. Requires `setValueIf`.
        setValueIf (str | None): Expression with a condition to set the value of the question. Requires `setValueExpression`.
        showCommentArea (bool): Whether to show the comment area. Doesn't work with `showOtherItem`.
        showDontKnowItem: bool = False
        showNoneItem: bool = False
        showOtherItem (bool): Whether to show the 'Other' item. Doesn't work with `showCommentArea`.
        showOtherItem: bool = False
        showRefuseItem: bool = False
        showSelectAllItem (bool | None): Whether to show the 'Select All' item.
        startWithNewLine (bool): Whether to start the question on a new line.
        state (str | None): If the question should be collapsed or expanded. Can be 'default', 'collapsed', 'expanded'.
        titleLocation (str): The location of the title. Can be 'default', 'top', 'bottom', 'left', 'hidden'.
        useDisplayValuesInDynamicTexts (bool): Whether to use display names for question values in placeholders.
        validators (ValidatorModel | list[ValidatorModel] | None): Validator(s) for the question.
        visible (bool): Whether the question is visible.
        visibleIf (str | None): Expression to make the question visible.
        width (str): Width of the question in CSS units.
        addCode (dict | None): Additional code for the question. Usually not necessary.
        customCode (str | None): Custom JS commands to be added to the survey.
        customFunctions (str | None): Custom JS functions definitions to be added to the survey. To be used with `customCode`.
    """
    args = {
        "titleLocation": titleLocation,
        "description": description,
        "descriptionLocation": descriptionLocation,
        "isRequired": isRequired,
        "readOnly": readOnly,
        "visible": visible,
        "requiredIf": requiredIf,
        "enableIf": enableIf,
        "visibleIf": visibleIf,
        "validators": validators,
        "showOtherItem": showOtherItem,
        "showCommentArea": showCommentArea,
        "commentPlaceholder": commentPlaceholder,
        "commentText": commentText,
        "correctAnswer": correctAnswer,
        "defaultValue": defaultValue,
        "defaultValueExpression": defaultValueExpression,
        "requiredErrorText": requiredErrorText,
        "errorLocation": errorLocation,
        "hideNumber": hideNumber,
        "id": id,
        "maxWidth": maxWidth,
        "minWidth": minWidth,
        "resetValueIf": resetValueIf,
        "setValueIf": setValueIf,
        "setValueExpression": setValueExpression,
        "startWithNewLine": startWithNewLine,
        "state": state,
        "useDisplayValuesInDynamicTexts": useDisplayValuesInDynamicTexts,
        "width": width,
        "addCode": addCode,
        "choicesFromQuestion": choicesFromQuestion,
        "choicesFromQuestionMode": choicesFromQuestionMode,
        "choicesOrder": choicesOrder,
        "showDontKnowItem": showDontKnowItem,
        "dontKnowText": dontKnowText,
        "hideIfChoicesEmpty": hideIfChoicesEmpty,
        "showNoneItem": showNoneItem,
        "noneText": noneText,
        "otherText": otherText,
        "otherErrorText": otherErrorText,
        "showRefuseItem": showRefuseItem,
        "refuseText": refuseText,
        "colCount": colCount,
        "isAllSelected": isAllSelected,
        "maxSelectedChoices": maxSelectedChoices,
        "minSelectedChoices": minSelectedChoices,
        "selectAllText": selectAllText,
        "showSelectAllItem": showSelectAllItem,
    }
    choices = flatten(choices)
    if not isinstance(title, list):
        title = [title]
    if len(title) != 1:
        return [
            QuestionCheckboxModel(
                name=f"{name}_{i+1}", title=t, choices=choices, **args, **kwargs
            )
            for i, t in enumerate(title)
        ]
    else:
        return QuestionCheckboxModel(
            name=name, title=title[0], choices=choices, **args, **kwargs
        )


def ranking(
    name: str,
    title: str | list[str] | None,
    *choices: str | dict | list,
    titleLocation: str = "default",
    description: str | None = None,
    descriptionLocation: str = "default",
    isRequired: bool = False,
    readOnly: bool = False,
    visible: bool = True,
    requiredIf: str | None = None,
    enableIf: str | None = None,
    visibleIf: str | None = None,
    validators: ValidatorModel | list[ValidatorModel] | None = None,
    showOtherItem: bool = False,
    showCommentArea: bool = False,
    commentPlaceholder: str | None = None,
    commentText: str | None = None,
    correctAnswer: str | None = None,
    defaultValue: str | None = None,
    defaultValueExpression: str | None = None,
    requiredErrorText: str | None = None,
    errorLocation: str = "default",
    hideNumber: bool = False,
    id: str | None = None,
    maxWidth: str = "100%",
    minWidth: str = "300px",
    resetValueIf: str | None = None,
    setValueIf: str | None = None,
    setValueExpression: str | None = None,
    startWithNewLine: bool = True,
    state: str = "default",
    useDisplayValuesInDynamicTexts: bool = True,
    width: str = "",
    addCode: dict | None = None,
    choicesFromQuestion: str | None = None,
    choicesFromQuestionMode: str = "all",
    choicesOrder: str = "none",
    showDontKnowItem: bool = False,
    dontKnowText: str | None = None,
    hideIfChoicesEmpty: bool | None = None,
    showNoneItem: bool = False,
    noneText: str | None = None,
    otherText: str | None = None,
    otherErrorText: str | None = None,
    showRefuseItem: bool = False,
    refuseText: str | None = None,
    colCount: int | None = None,
    isAllSelected: bool | None = None,
    maxSelectedChoices: int = 0,
    minSelectedChoices: int = 0,
    selectAllText: str | None = None,
    showSelectAllItem: bool | None = None,
    longTap: bool = True,
    selectToRankAreasLayout: str = "horizontal",
    selectToRankEmptyRankedAreaText: str | None = None,
    selectToRankEmptyUnrankedAreaText: str | None = None,
    selectToRankEnabled: bool = False,
    **kwargs,
) -> QuestionRankingModel | list[QuestionRankingModel]:
    """Create a ranking question object

    Args:
        name (str): The label of the question.
        title (str | None): The visible title of the question. If None, `name` is used.
        choices (str | dict | list): The choices for the question. Can be string(s) or dictionary(-ies) with structure `{"value": ..., "text": ...}`. You can also add `visibleIf`, `enableIf`, and `requiredIf` to the dictionary.
        choicesFromQuestion (str | None): The name of the question to get the choices from if the are to be copied. Use with `choicesFromQuestionMode`.
        choicesFromQuestionMode (str): The mode of copying choices. Can be 'all', 'selected', 'unselected'.
        choicesOrder (str): The order of the choices. Can be 'none', 'asc', 'desc', 'random'.
        colCount (int | None): The number of columns for the choices. 0 means a single line.
        commentPlaceholder (str | None): Placeholder text for the comment area.
        commentText (str | None): Text for the comment area.
        correctAnswer (str | None): Correct answer for the question. Use for quizzes.
        defaultValue (str | None): Default value for the question.
        defaultValueExpression (str | None): Expression deciding the default value for the question.
        description (str | None): Optional subtitle or description of the question.
        descriptionLocation (str): The location of the description. Can be 'default', 'underTitle', 'underInput'.
        dontKnowText: str | None = None
        enableIf (str | None): Expression to enable the question.
        errorLocation (str | None): Location of the error text. Can be 'default' 'top', 'bottom'.
        hideIfChoicesEmpty: bool | None = None
        hideNumber (bool): Whether to hide the question number.
        id (str | None): HTML id attribute for the question. Usually not necessary.
        isAllSelected (bool | None): Start with all choices selected. Default is False.
        longTap (bool): Whether to use long tap for dragging on mobile devices.
        maxSelectedChoices (int): Maximum number of selected choices. 0 means no limit.
        maxWidth (str): Maximum width of the question in CSS units.
        minSelectedChoices (int): Minimum number of selected choices. 0 means no limit.
        minWidth (str): Minimum width of the question in CSS units.
        noneText: str | None = None
        otherErrorText: str | None = None
        otherText: str | None = None
        readOnly (bool): Whether the question is read-only.
        refuseText: str | None = None
        isRequired (bool): Whether the question is required.
        requiredErrorText (str | None): Error text if the required condition is not met.
        requiredIf (str | None): Expression to make the question required.
        resetValueIf (str | None): Expression to reset the value of the question.
        selectAllText (str | None): Text for the 'Select All' item.
        selectToRankAreasLayout (str): The layout of the ranked and unranked areas when `selectToRankEnabled=True`. Can be 'horizontal', 'vertical'.
        selectToRankEmptyRankedAreaText (str | None): Text for the empty ranked area when `selectToRankEnabled=True`.
        selectToRankEmptyUnrankedAreaText (str | None): Text for the empty unranked area when `selectToRankEnabled=True`.
        selectToRankEnabled (bool): Whether user should select items they want to rank before ranking them. Default is False.
        setValueExpression (str | None): Expression to decide on the value of the question to be set. Requires `setValueIf`.
        setValueIf (str | None): Expression with a condition to set the value of the question. Requires `setValueExpression`.
        showCommentArea (bool): Whether to show the comment area. Doesn't work with `showOtherItem`.
        showDontKnowItem: bool = False
        showNoneItem: bool = False
        showOtherItem (bool): Whether to show the 'Other' item. Doesn't work with `showCommentArea`.
        showOtherItem: bool = False
        showRefuseItem: bool = False
        showSelectAllItem (bool | None): Whether to show the 'Select All' item.
        startWithNewLine (bool): Whether to start the question on a new line.
        state (str | None): If the question should be collapsed or expanded. Can be 'default', 'collapsed', 'expanded'.
        titleLocation (str): The location of the title. Can be 'default', 'top', 'bottom', 'left', 'hidden'.
        useDisplayValuesInDynamicTexts (bool): Whether to use display names for question values in placeholders.
        validators (ValidatorModel | list[ValidatorModel] | None): Validator(s) for the question.
        visible (bool): Whether the question is visible.
        visibleIf (str | None): Expression to make the question visible.
        width (str): Width of the question in CSS units.
        addCode (dict | None): Additional code for the question. Usually not necessary.
        customCode (str | None): Custom JS commands to be added to the survey.
        customFunctions (str | None): Custom JS functions definitions to be added to the survey. To be used with `customCode`.
    """
    args = {
        "titleLocation": titleLocation,
        "description": description,
        "descriptionLocation": descriptionLocation,
        "isRequired": isRequired,
        "readOnly": readOnly,
        "visible": visible,
        "requiredIf": requiredIf,
        "enableIf": enableIf,
        "visibleIf": visibleIf,
        "validators": validators,
        "showOtherItem": showOtherItem,
        "showCommentArea": showCommentArea,
        "commentPlaceholder": commentPlaceholder,
        "commentText": commentText,
        "correctAnswer": correctAnswer,
        "defaultValue": defaultValue,
        "defaultValueExpression": defaultValueExpression,
        "requiredErrorText": requiredErrorText,
        "errorLocation": errorLocation,
        "hideNumber": hideNumber,
        "id": id,
        "maxWidth": maxWidth,
        "minWidth": minWidth,
        "resetValueIf": resetValueIf,
        "setValueIf": setValueIf,
        "setValueExpression": setValueExpression,
        "startWithNewLine": startWithNewLine,
        "state": state,
        "useDisplayValuesInDynamicTexts": useDisplayValuesInDynamicTexts,
        "width": width,
        "addCode": addCode,
        "choicesFromQuestion": choicesFromQuestion,
        "choicesFromQuestionMode": choicesFromQuestionMode,
        "choicesOrder": choicesOrder,
        "showDontKnowItem": showDontKnowItem,
        "dontKnowText": dontKnowText,
        "hideIfChoicesEmpty": hideIfChoicesEmpty,
        "showNoneItem": showNoneItem,
        "noneText": noneText,
        "otherText": otherText,
        "otherErrorText": otherErrorText,
        "showRefuseItem": showRefuseItem,
        "refuseText": refuseText,
        "colCount": colCount,
        "isAllSelected": isAllSelected,
        "maxSelectedChoices": maxSelectedChoices,
        "minSelectedChoices": minSelectedChoices,
        "selectAllText": selectAllText,
        "showSelectAllItem": showSelectAllItem,
        "longTap": longTap,
        "selectToRankAreasLayout": selectToRankAreasLayout,
        "selectToRankEmptyRankedAreaText": selectToRankEmptyRankedAreaText,
        "selectToRankEmptyUnrankedAreaText": selectToRankEmptyUnrankedAreaText,
        "selectToRankEnabled": selectToRankEnabled,
    }
    choices = flatten(choices)
    if not isinstance(title, list):
        title = [title]
    if len(title) != 1:
        return [
            QuestionRankingModel(
                name=f"{name}_{i+1}", title=t, choices=choices, **args, **kwargs
            )
            for i, t in enumerate(title)
        ]
    else:
        return QuestionRankingModel(
            name=name, title=title[0], choices=choices, **args, **kwargs
        )


def radio(
    name: str,
    title: str | list[str] | None,
    *choices: str | dict | list,
    titleLocation: str = "default",
    description: str | None = None,
    descriptionLocation: str = "default",
    isRequired: bool = False,
    readOnly: bool = False,
    visible: bool = True,
    requiredIf: str | None = None,
    enableIf: str | None = None,
    visibleIf: str | None = None,
    validators: ValidatorModel | list[ValidatorModel] | None = None,
    showOtherItem: bool = False,
    showCommentArea: bool = False,
    commentPlaceholder: str | None = None,
    commentText: str | None = None,
    correctAnswer: str | None = None,
    defaultValue: str | None = None,
    defaultValueExpression: str | None = None,
    requiredErrorText: str | None = None,
    errorLocation: str = "default",
    hideNumber: bool = False,
    id: str | None = None,
    maxWidth: str = "100%",
    minWidth: str = "300px",
    resetValueIf: str | None = None,
    setValueIf: str | None = None,
    setValueExpression: str | None = None,
    startWithNewLine: bool = True,
    state: str = "default",
    useDisplayValuesInDynamicTexts: bool = True,
    width: str = "",
    addCode: dict | None = None,
    choicesFromQuestion: str | None = None,
    choicesFromQuestionMode: str = "all",
    choicesOrder: str = "none",
    showDontKnowItem: bool = False,
    dontKnowText: str | None = None,
    hideIfChoicesEmpty: bool | None = None,
    showNoneItem: bool = False,
    noneText: str | None = None,
    otherText: str | None = None,
    otherErrorText: str | None = None,
    showRefuseItem: bool = False,
    refuseText: str | None = None,
    colCount: int | None = None,
    showClearButton: bool = False,
    **kwargs,
) -> QuestionRadiogroupModel | list[QuestionRadiogroupModel]:
    """Create a radio question object

    Args:
        name (str): The label of the question.
        title (str | None): The visible title of the question. If None, `name` is used.
        choices (str | dict | list): The choices for the question. Can be string(s) or dictionary(-ies) with structure `{"value": ..., "text": ...}`. You can also add `visibleIf`, `enableIf`, and `requiredIf` to the dictionary.
        choicesFromQuestion (str | None): The name of the question to get the choices from if the are to be copied. Use with `choicesFromQuestionMode`.
        choicesFromQuestionMode (str): The mode of copying choices. Can be 'all', 'selected', 'unselected'.
        choicesOrder (str): The order of the choices. Can be 'none', 'asc', 'desc', 'random'.
        commentPlaceholder (str | None): Placeholder text for the comment area.
        commentText (str | None): Text for the comment area.
        correctAnswer (str | None): Correct answer for the question. Use for quizzes.
        colCount (int | None): The number of columns for the choices. 0 means a single line.
        defaultValue (str | None): Default value for the question.
        defaultValueExpression (str | None): Expression deciding the default value for the question.
        description (str | None): Optional subtitle or description of the question.
        descriptionLocation (str): The location of the description. Can be 'default', 'underTitle', 'underInput'.
        dontKnowText: str | None = None
        enableIf (str | None): Expression to enable the question.
        errorLocation (str | None): Location of the error text. Can be 'default' 'top', 'bottom'.
        hideIfChoicesEmpty: bool | None = None
        hideNumber (bool): Whether to hide the question number.
        id (str | None): HTML id attribute for the question. Usually not necessary.
        maxWidth (str): Maximum width of the question in CSS units.
        minWidth (str): Minimum width of the question in CSS units.
        noneText: str | None = None
        otherErrorText: str | None = None
        otherText: str | None = None
        readOnly (bool): Whether the question is read-only.
        refuseText: str | None = None
        isRequired (bool): Whether the question is required.
        requiredErrorText (str | None): Error text if the required condition is not met.
        requiredIf (str | None): Expression to make the question required.
        resetValueIf (str | None): Expression to reset the value of the question.
        setValueExpression (str | None): Expression to decide on the value of the question to be set. Requires `setValueIf`.
        setValueIf (str | None): Expression with a condition to set the value of the question. Requires `setValueExpression`.
        showClearButton (bool): Show a button to clear the answer.
        showCommentArea (bool): Whether to show the comment area. Doesn't work with `showOtherItem`.
        showDontKnowItem: bool = False
        showNoneItem: bool = False
        showOtherItem (bool): Whether to show the 'Other' item. Doesn't work with `showCommentArea`.
        showOtherItem: bool = False
        showRefuseItem: bool = False
        startWithNewLine (bool): Whether to start the question on a new line.
        state (str | None): If the question should be collapsed or expanded. Can be 'default', 'collapsed', 'expanded'.
        titleLocation (str): The location of the title. Can be 'default', 'top', 'bottom', 'left', 'hidden'.
        useDisplayValuesInDynamicTexts (bool): Whether to use display names for question values in placeholders.
        validators (ValidatorModel | list[ValidatorModel] | None): Validator(s) for the question.
        visible (bool): Whether the question is visible.
        visibleIf (str | None): Expression to make the question visible.
        width (str): Width of the question in CSS units.
        addCode (dict | None): Additional code for the question. Usually not necessary.
        customCode (str | None): Custom JS commands to be added to the survey.
        customFunctions (str | None): Custom JS functions definitions to be added to the survey. To be used with `customCode`.

    Returns:
        QuestionRadiogroupModel: The question object model or a list of question object models if `title` is a list.
    """
    args = {
        "titleLocation": titleLocation,
        "description": description,
        "descriptionLocation": descriptionLocation,
        "isRequired": isRequired,
        "readOnly": readOnly,
        "visible": visible,
        "requiredIf": requiredIf,
        "enableIf": enableIf,
        "visibleIf": visibleIf,
        "validators": validators,
        "showOtherItem": showOtherItem,
        "showCommentArea": showCommentArea,
        "commentPlaceholder": commentPlaceholder,
        "commentText": commentText,
        "correctAnswer": correctAnswer,
        "defaultValue": defaultValue,
        "defaultValueExpression": defaultValueExpression,
        "requiredErrorText": requiredErrorText,
        "errorLocation": errorLocation,
        "hideNumber": hideNumber,
        "id": id,
        "maxWidth": maxWidth,
        "minWidth": minWidth,
        "resetValueIf": resetValueIf,
        "setValueIf": setValueIf,
        "setValueExpression": setValueExpression,
        "startWithNewLine": startWithNewLine,
        "state": state,
        "useDisplayValuesInDynamicTexts": useDisplayValuesInDynamicTexts,
        "width": width,
        "addCode": addCode,
        "choicesFromQuestion": choicesFromQuestion,
        "choicesFromQuestionMode": choicesFromQuestionMode,
        "choicesOrder": choicesOrder,
        "showDontKnowItem": showDontKnowItem,
        "dontKnowText": dontKnowText,
        "hideIfChoicesEmpty": hideIfChoicesEmpty,
        "showNoneItem": showNoneItem,
        "noneText": noneText,
        "otherText": otherText,
        "otherErrorText": otherErrorText,
        "showRefuseItem": showRefuseItem,
        "refuseText": refuseText,
        "colCount": colCount,
        "showClearButton": showClearButton,
    }
    choices = flatten(choices)
    if not isinstance(title, list):
        title = [title]
    if len(title) != 1:
        return [
            QuestionRadiogroupModel(
                name=f"{name}_{i+1}", title=t, choices=choices, **args, **kwargs
            )
            for i, t in enumerate(title)
        ]
    else:
        return QuestionRadiogroupModel(
            name=name, title=title[0], choices=choices, **args, **kwargs
        )


def dropdownMultiple(
    name: str,
    title: str | list[str] | None,
    *choices: str | dict | list,
    titleLocation: str = "default",
    description: str | None = None,
    descriptionLocation: str = "default",
    isRequired: bool = False,
    readOnly: bool = False,
    visible: bool = True,
    requiredIf: str | None = None,
    enableIf: str | None = None,
    visibleIf: str | None = None,
    validators: ValidatorModel | list[ValidatorModel] | None = None,
    showOtherItem: bool = False,
    showCommentArea: bool = False,
    commentPlaceholder: str | None = None,
    commentText: str | None = None,
    correctAnswer: str | None = None,
    defaultValue: str | None = None,
    defaultValueExpression: str | None = None,
    requiredErrorText: str | None = None,
    errorLocation: str = "default",
    hideNumber: bool = False,
    id: str | None = None,
    maxWidth: str = "100%",
    minWidth: str = "300px",
    resetValueIf: str | None = None,
    setValueIf: str | None = None,
    setValueExpression: str | None = None,
    startWithNewLine: bool = True,
    state: str = "default",
    useDisplayValuesInDynamicTexts: bool = True,
    width: str = "",
    addCode: dict | None = None,
    choicesFromQuestion: str | None = None,
    choicesFromQuestionMode: str = "all",
    choicesOrder: str = "none",
    showDontKnowItem: bool = False,
    dontKnowText: str | None = None,
    hideIfChoicesEmpty: bool | None = None,
    showNoneItem: bool = False,
    noneText: str | None = None,
    otherText: str | None = None,
    otherErrorText: str | None = None,
    showRefuseItem: bool = False,
    refuseText: str | None = None,
    colCount: int | None = None,
    isAllSelected: bool | None = None,
    maxSelectedChoices: int = 0,
    minSelectedChoices: int = 0,
    selectAllText: str | None = None,
    showSelectAllItem: bool | None = None,
    allowClear: bool = True,
    closeOnSelect: int | None = None,
    hideSelectedItems: bool | None = False,
    placeholder: str | None = None,
    searchEnabled: bool = True,
    searchMode: str = "contains",
    **kwargs,
) -> QuestionTagboxModel | list[QuestionTagboxModel]:
    """Create a multiple dropdown question object

    Args:
        name (str): The label of the question.
        title (str | None): The visible title of the question. If None, `name` is used.
        choices (str | dict | list): The choices for the question. Can be string(s) or dictionary(-ies) with structure `{"value": ..., "text": ...}`. You can also add `visibleIf`, `enableIf`, and `requiredIf` to the dictionary.
        allowClear (str): Whether to show the 'Clear' button for each answer.
        choicesFromQuestion (str | None): The name of the question to get the choices from if the are to be copied. Use with `choicesFromQuestionMode`.
        choicesFromQuestionMode (str): The mode of copying choices. Can be 'all', 'selected', 'unselected'.
        choicesOrder (str): The order of the choices. Can be 'none', 'asc', 'desc', 'random'.
        closeOnSelect (int | None): Whether to close the dropdown after user selects a specified number of items.
        colCount (int | None): The number of columns for the choices. 0 means a single line.
        commentPlaceholder (str | None): Placeholder text for the comment area.
        commentText (str | None): Text for the comment area.
        correctAnswer (str | None): Correct answer for the question. Use for quizzes.
        defaultValue (str | None): Default value for the question.
        defaultValueExpression (str | None): Expression deciding the default value for the question.
        description (str | None): Optional subtitle or description of the question.
        descriptionLocation (str): The location of the description. Can be 'default', 'underTitle', 'underInput'.
        dontKnowText: str | None = None
        enableIf (str | None): Expression to enable the question.
        errorLocation (str | None): Location of the error text. Can be 'default' 'top', 'bottom'.
        hideIfChoicesEmpty: bool | None = None
        hideNumber (bool): Whether to hide the question number.
        hideSelectedItems (bool | None): Whether to hide selected items in the dropdown.
        id (str | None): HTML id attribute for the question. Usually not necessary.
        isAllSelected (bool | None): Start with all choices selected. Default is False.
        maxSelectedChoices (int): Maximum number of selected choices. 0 means no limit.
        maxWidth (str): Maximum width of the question in CSS units.
        minSelectedChoices (int): Minimum number of selected choices. 0 means no limit.
        minWidth (str): Minimum width of the question in CSS units.
        noneText: str | None = None
        otherErrorText: str | None = None
        otherText: str | None = None
        placeholder (str | None): Placeholder text for the input with no value.
        readOnly (bool): Whether the question is read-only.
        refuseText: str | None = None
        isRequired (bool): Whether the question is required.
        requiredErrorText (str | None): Error text if the required condition is not met.
        requiredIf (str | None): Expression to make the question required.
        resetValueIf (str | None): Expression to reset the value of the question.
        searchEnabled (bool): Whether to enable search in the dropdown.
        searchMode (str): The search mode. Can be 'contains' (default), 'startsWith'. Works only if `searchEnabled=True`.
        selectAllText (str | None): Text for the 'Select All' item.
        setValueExpression (str | None): Expression to decide on the value of the question to be set. Requires `setValueIf`.
        setValueIf (str | None): Expression with a condition to set the value of the question. Requires `setValueExpression`.
        showCommentArea (bool): Whether to show the comment area. Doesn't work with `showOtherItem`.
        showDontKnowItem: bool = False
        showNoneItem: bool = False
        showOtherItem (bool): Whether to show the 'Other' item. Doesn't work with `showCommentArea`.
        showOtherItem: bool = False
        showRefuseItem: bool = False
        showSelectAllItem (bool | None): Whether to show the 'Select All' item.
        startWithNewLine (bool): Whether to start the question on a new line.
        state (str | None): If the question should be collapsed or expanded. Can be 'default', 'collapsed', 'expanded'.
        titleLocation (str): The location of the title. Can be 'default', 'top', 'bottom', 'left', 'hidden'.
        useDisplayValuesInDynamicTexts (bool): Whether to use display names for question values in placeholders.
        validators (ValidatorModel | list[ValidatorModel] | None): Validator(s) for the question.
        visible (bool): Whether the question is visible.
        visibleIf (str | None): Expression to make the question visible.
        width (str): Width of the question in CSS units.
        addCode (dict | None): Additional code for the question. Usually not necessary.
        customCode (str | None): Custom JS commands to be added to the survey.
        customFunctions (str | None): Custom JS functions definitions to be added to the survey. To be used with `customCode`.
    """
    args = {
        "titleLocation": titleLocation,
        "description": description,
        "descriptionLocation": descriptionLocation,
        "isRequired": isRequired,
        "readOnly": readOnly,
        "visible": visible,
        "requiredIf": requiredIf,
        "enableIf": enableIf,
        "visibleIf": visibleIf,
        "validators": validators,
        "showOtherItem": showOtherItem,
        "showCommentArea": showCommentArea,
        "commentPlaceholder": commentPlaceholder,
        "commentText": commentText,
        "correctAnswer": correctAnswer,
        "defaultValue": defaultValue,
        "defaultValueExpression": defaultValueExpression,
        "requiredErrorText": requiredErrorText,
        "errorLocation": errorLocation,
        "hideNumber": hideNumber,
        "id": id,
        "maxWidth": maxWidth,
        "minWidth": minWidth,
        "resetValueIf": resetValueIf,
        "setValueIf": setValueIf,
        "setValueExpression": setValueExpression,
        "startWithNewLine": startWithNewLine,
        "state": state,
        "useDisplayValuesInDynamicTexts": useDisplayValuesInDynamicTexts,
        "width": width,
        "addCode": addCode,
        "choicesFromQuestion": choicesFromQuestion,
        "choicesFromQuestionMode": choicesFromQuestionMode,
        "choicesOrder": choicesOrder,
        "showDontKnowItem": showDontKnowItem,
        "dontKnowText": dontKnowText,
        "hideIfChoicesEmpty": hideIfChoicesEmpty,
        "showNoneItem": showNoneItem,
        "noneText": noneText,
        "otherText": otherText,
        "otherErrorText": otherErrorText,
        "showRefuseItem": showRefuseItem,
        "refuseText": refuseText,
        "colCount": colCount,
        "isAllSelected": isAllSelected,
        "maxSelectedChoices": maxSelectedChoices,
        "minSelectedChoices": minSelectedChoices,
        "selectAllText": selectAllText,
        "showSelectAllItem": showSelectAllItem,
        "allowClear": allowClear,
        "closeOnSelect": closeOnSelect,
        "hideSelectedItems": hideSelectedItems,
        "placeholder": placeholder,
        "searchEnabled": searchEnabled,
        "searchMode": searchMode,
    }
    choices = flatten(choices)
    if not isinstance(title, list):
        title = [title]
    if len(title) != 1:
        return [
            QuestionTagboxModel(
                name=f"{name}_{i+1}", title=t, choices=choices, **args, **kwargs
            )
            for i, t in enumerate(title)
        ]
    else:
        return QuestionTagboxModel(
            name=name, title=title[0], choices=choices, **args, **kwargs
        )


def textLong(
    name: str,
    *title: str | list[str] | None,
    titleLocation: str = "default",
    description: str | None = None,
    descriptionLocation: str = "default",
    isRequired: bool = False,
    readOnly: bool = False,
    visible: bool = True,
    requiredIf: str | None = None,
    enableIf: str | None = None,
    visibleIf: str | None = None,
    validators: ValidatorModel | list[ValidatorModel] | None = None,
    showOtherItem: bool = False,
    showCommentArea: bool = False,
    commentPlaceholder: str | None = None,
    commentText: str | None = None,
    correctAnswer: str | None = None,
    defaultValue: str | None = None,
    defaultValueExpression: str | None = None,
    requiredErrorText: str | None = None,
    errorLocation: str = "default",
    hideNumber: bool = False,
    id: str | None = None,
    maxWidth: str = "100%",
    minWidth: str = "300px",
    monitorInput: bool = False,
    resetValueIf: str | None = None,
    setValueIf: str | None = None,
    setValueExpression: str | None = None,
    startWithNewLine: bool = True,
    state: str = "default",
    useDisplayValuesInDynamicTexts: bool = True,
    width: str = "",
    addCode: dict | None = None,
    acceptCarriageReturn: bool = True,
    allowResize: bool | None = None,
    autoGrow: bool | None = None,
    rows: int = 4,
    **kwargs,
) -> QuestionCommentModel | list[QuestionCommentModel]:
    """Create a long text question object

    Attributes:
        name (str): The label of the question.
        title (str | None): The visible title of the question. If None, `name` is used.
        acceptCarriageReturn (bool): Whether to allow line breaks. Default is True.
        allowResize (bool): Whether to allow resizing the input field. Default is True.
        autoGrow (bool): Whether to automatically grow the input field. Default is False.
        commentPlaceholder (str | None): Placeholder text for the comment area.
        commentText (str | None): Text for the comment area.
        correctAnswer (str | None): Correct answer for the question. Use for quizzes.
        defaultValue (str | None): Default value for the question.
        defaultValueExpression (str | None): Expression deciding the default value for the question.
        description (str | None): Optional subtitle or description of the question.
        descriptionLocation (str): The location of the description. Can be 'default', 'underTitle', 'underInput'.
        enableIf (str | None): Expression to enable the question.
        errorLocation (str | None): Location of the error text. Can be 'default' 'top', 'bottom'.
        hideNumber (bool): Whether to hide the question number.
        id (str | None): HTML id attribute for the question. Usually not necessary.
        maxWidth (str): Maximum width of the question in CSS units.
        minWidth (str): Minimum width of the question in CSS units.
        monitorInput (bool): Whether to count the time spent with the question focused and the number of key presses. Useful for bot detection.
        readOnly (bool): Whether the question is read-only.
        isRequired (bool): Whether the question is required.
        requiredErrorText (str | None): Error text if the required condition is not met.
        requiredIf (str | None): Expression to make the question required.
        resetValueIf (str | None): Expression to reset the value of the question.
        rows (int): Height of the input field in rows' number.
        setValueExpression (str | None): Expression to decide on the value of the question to be set. Requires `setValueIf`.
        setValueIf (str | None): Expression with a condition to set the value of the question. Requires `setValueExpression`.
        showCommentArea (bool): Whether to show the comment area. Doesn't work with `showOtherItem`.
        showOtherItem (bool): Whether to show the 'Other' item. Doesn't work with `showCommentArea`.
        startWithNewLine (bool): Whether to start the question on a new line.
        state (str | None): If the question should be collapsed or expanded. Can be 'default', 'collapsed', 'expanded'.
        titleLocation (str): The location of the title. Can be 'default', 'top', 'bottom', 'left', 'hidden'.
        useDisplayValuesInDynamicTexts (bool): Whether to use display names for question values in placeholders.
        validators (ValidatorModel | list[ValidatorModel] | None): Validator(s) for the question.
        visible (bool): Whether the question is visible.
        visibleIf (str | None): Expression to make the question visible.
        width (str): Width of the question in CSS units.
        addCode (dict | None): Additional code for the question. Usually not necessary.
        customCode (str | None): Custom JS commands to be added to the survey.
        customFunctions (str | None): Custom JS functions definitions to be added to the survey. To be used with `customCode`.
    """
    args = {
        "titleLocation": titleLocation,
        "description": description,
        "descriptionLocation": descriptionLocation,
        "isRequired": isRequired,
        "readOnly": readOnly,
        "visible": visible,
        "requiredIf": requiredIf,
        "enableIf": enableIf,
        "visibleIf": visibleIf,
        "validators": validators,
        "showOtherItem": showOtherItem,
        "showCommentArea": showCommentArea,
        "commentPlaceholder": commentPlaceholder,
        "commentText": commentText,
        "correctAnswer": correctAnswer,
        "defaultValue": defaultValue,
        "defaultValueExpression": defaultValueExpression,
        "requiredErrorText": requiredErrorText,
        "errorLocation": errorLocation,
        "hideNumber": hideNumber,
        "id": id,
        "maxWidth": maxWidth,
        "minWidth": minWidth,
        "monitorInput": monitorInput,
        "resetValueIf": resetValueIf,
        "setValueIf": setValueIf,
        "setValueExpression": setValueExpression,
        "startWithNewLine": startWithNewLine,
        "state": state,
        "useDisplayValuesInDynamicTexts": useDisplayValuesInDynamicTexts,
        "width": width,
        "addCode": addCode,
        "acceptCarriageReturn": acceptCarriageReturn,
        "allowResize": allowResize,
        "autoGrow": autoGrow,
        "rows": rows,
    }
    title = flatten(title)
    if len(title) != 1:
        return [
            QuestionCommentModel(name=f"{name}_{i+1}", title=t, **args, **kwargs)
            for i, t in enumerate(title)
        ]
    return QuestionCommentModel(name=name, title=title[0], **args, **kwargs)


def rating(
    name: str,
    *title: str | list[str] | None,
    titleLocation: str = "default",
    description: str | None = None,
    descriptionLocation: str = "default",
    isRequired: bool = False,
    readOnly: bool = False,
    visible: bool = True,
    requiredIf: str | None = None,
    enableIf: str | None = None,
    visibleIf: str | None = None,
    validators: ValidatorModel | list[ValidatorModel] | None = None,
    showOtherItem: bool = False,
    showCommentArea: bool = False,
    commentPlaceholder: str | None = None,
    commentText: str | None = None,
    correctAnswer: str | None = None,
    defaultValue: str | None = None,
    defaultValueExpression: str | None = None,
    requiredErrorText: str | None = None,
    errorLocation: str = "default",
    hideNumber: bool = False,
    id: str | None = None,
    maxWidth: str = "100%",
    minWidth: str = "300px",
    resetValueIf: str | None = None,
    setValueIf: str | None = None,
    setValueExpression: str | None = None,
    startWithNewLine: bool = True,
    state: str = "default",
    useDisplayValuesInDynamicTexts: bool = True,
    width: str = "",
    addCode: dict | None = None,
    maxRateDescription: str | None = None,
    minRateDescription: str | None = None,
    rateMax: int = 5,
    rateMin: int = 1,
    rateStep: int = 1,
    rateType: str = "labels",
    rateValues: list | None = None,
    scaleColorMode: str = "monochrome",
    **kwargs,
) -> QuestionRatingModel | list[QuestionRatingModel]:
    """Create a rating question object

    Attributes:
        name (str): The label of the question.
        title (str | None): The visible title of the question. If None, `name` is used.
        commentPlaceholder (str | None): Placeholder text for the comment area.
        commentText (str | None): Text for the comment area.
        correctAnswer (str | None): Correct answer for the question. Use for quizzes.
        defaultValue (str | None): Default value for the question.
        defaultValueExpression (str | None): Expression deciding the default value for the question.
        description (str | None): Optional subtitle or description of the question.
        descriptionLocation (str): The location of the description. Can be 'default', 'underTitle', 'underInput'.
        enableIf (str | None): Expression to enable the question.
        errorLocation (str | None): Location of the error text. Can be 'default' 'top', 'bottom'.
        hideNumber (bool): Whether to hide the question number.
        id (str | None): HTML id attribute for the question. Usually not necessary.
        maxRateDescription (str | None): Description for the biggest rate.
        maxWidth (str): Maximum width of the question in CSS units.
        minRateDescription (str | None): Description for the smallest rate.
        minWidth (str): Minimum width of the question in CSS units.
        rateMax (int): Maximum rate. Works only if `rateValues` is not set.
        rateMin (int): Minimum rate. Works only if `rateValues` is not set.
        rateStep (int): Step for the rate. Works only if `rateValues` is not set.
        rateType (str): The type of the rate. Can be 'labels', 'stars', 'smileys'.
        rateValues (list | None): Manually set rate values. Use a list of primitives and/or dictionaries `{"value": ..., "text": ...}`.
        readOnly (bool): Whether the question is read-only.
        isRequired (bool): Whether the question is required.
        requiredErrorText (str | None): Error text if the required condition is not met.
        requiredIf (str | None): Expression to make the question required.
        resetValueIf (str | None): Expression to reset the value of the question.
        scaleColorMode (str): The color mode of the scale if `rateType='smileys'`. Can be 'monochrome', 'colored'.
        setValueExpression (str | None): Expression to decide on the value of the question to be set. Requires `setValueIf`.
        setValueIf (str | None): Expression with a condition to set the value of the question. Requires `setValueExpression`.
        showCommentArea (bool): Whether to show the comment area. Doesn't work with `showOtherItem`.
        showOtherItem (bool): Whether to show the 'Other' item. Doesn't work with `showCommentArea`.
        startWithNewLine (bool): Whether to start the question on a new line.
        state (str | None): If the question should be collapsed or expanded. Can be 'default', 'collapsed', 'expanded'.
        titleLocation (str): The location of the title. Can be 'default', 'top', 'bottom', 'left', 'hidden'.
        useDisplayValuesInDynamicTexts (bool): Whether to use display names for question values in placeholders.
        validators (ValidatorModel | list[ValidatorModel] | None): Validator(s) for the question.
        visible (bool): Whether the question is visible.
        visibleIf (str | None): Expression to make the question visible.
        width (str): Width of the question in CSS units.
        addCode (dict | None): Additional code for the question. Usually not necessary.
        customCode (str | None): Custom JS commands to be added to the survey.
        customFunctions (str | None): Custom JS functions definitions to be added to the survey. To be used with `customCode`.
    """
    args = {
        "titleLocation": titleLocation,
        "description": description,
        "descriptionLocation": descriptionLocation,
        "isRequired": isRequired,
        "readOnly": readOnly,
        "visible": visible,
        "requiredIf": requiredIf,
        "enableIf": enableIf,
        "visibleIf": visibleIf,
        "validators": validators,
        "showOtherItem": showOtherItem,
        "showCommentArea": showCommentArea,
        "commentPlaceholder": commentPlaceholder,
        "commentText": commentText,
        "correctAnswer": correctAnswer,
        "defaultValue": defaultValue,
        "defaultValueExpression": defaultValueExpression,
        "requiredErrorText": requiredErrorText,
        "errorLocation": errorLocation,
        "hideNumber": hideNumber,
        "id": id,
        "maxWidth": maxWidth,
        "minWidth": minWidth,
        "resetValueIf": resetValueIf,
        "setValueIf": setValueIf,
        "setValueExpression": setValueExpression,
        "startWithNewLine": startWithNewLine,
        "state": state,
        "useDisplayValuesInDynamicTexts": useDisplayValuesInDynamicTexts,
        "width": width,
        "addCode": addCode,
        "maxRateDescription": maxRateDescription,
        "minRateDescription": minRateDescription,
        "rateMax": rateMax,
        "rateMin": rateMin,
        "rateStep": rateStep,
        "rateType": rateType,
        "rateValues": rateValues,
        "scaleColorMode": scaleColorMode,
    }
    title = flatten(title)
    if len(title) != 1:
        return [
            QuestionRatingModel(name=f"{name}_{i+1}", title=t, **args, **kwargs)
            for i, t in enumerate(title)
        ]
    return QuestionRatingModel(name=name, title=title[0], **args, **kwargs)


def yesno(
    name: str,
    *title: str | list[str] | None,
    titleLocation: str = "default",
    description: str | None = None,
    descriptionLocation: str = "default",
    isRequired: bool = False,
    readOnly: bool = False,
    visible: bool = True,
    requiredIf: str | None = None,
    enableIf: str | None = None,
    visibleIf: str | None = None,
    validators: ValidatorModel | list[ValidatorModel] | None = None,
    showOtherItem: bool = False,
    showCommentArea: bool = False,
    commentPlaceholder: str | None = None,
    commentText: str | None = None,
    correctAnswer: str | None = None,
    defaultValue: str | None = None,
    defaultValueExpression: str | None = None,
    requiredErrorText: str | None = None,
    errorLocation: str = "default",
    hideNumber: bool = False,
    id: str | None = None,
    maxWidth: str = "100%",
    minWidth: str = "300px",
    resetValueIf: str | None = None,
    setValueIf: str | None = None,
    setValueExpression: str | None = None,
    startWithNewLine: bool = True,
    state: str = "default",
    useDisplayValuesInDynamicTexts: bool = True,
    width: str = "",
    addCode: dict | None = None,
    labelFalse: str | None = None,
    labelTrue: str | None = None,
    swapOrder: bool = False,
    valueFalse: bool | str = False,
    valueTrue: bool | str = True,
    **kwargs,
) -> QuestionBooleanModel | list[QuestionBooleanModel]:
    """Create a yes/no (boolean) question object

    Attributes:
        name (str): The label of the question.
        title (str | None): The visible title of the question. If None, `name` is used.
        commentPlaceholder (str | None): Placeholder text for the comment area.
        commentText (str | None): Text for the comment area.
        correctAnswer (str | None): Correct answer for the question. Use for quizzes.
        defaultValue (str | None): Default value for the question.
        defaultValueExpression (str | None): Expression deciding the default value for the question.
        description (str | None): Optional subtitle or description of the question.
        descriptionLocation (str): The location of the description. Can be 'default', 'underTitle', 'underInput'.
        enableIf (str | None): Expression to enable the question.
        errorLocation (str | None): Location of the error text. Can be 'default' 'top', 'bottom'.
        hideNumber (bool): Whether to hide the question number.
        id (str | None): HTML id attribute for the question. Usually not necessary.
        labelFalse (str | None): Label for the 'false' value.
        labelTrue (str | None): Label for the 'true' value.
        maxWidth (str): Maximum width of the question in CSS units.
        minWidth (str): Minimum width of the question in CSS units.
        readOnly (bool): Whether the question is read-only.
        isRequired (bool): Whether the question is required.
        requiredErrorText (str | None): Error text if the required condition is not met.
        requiredIf (str | None): Expression to make the question required.
        resetValueIf (str | None): Expression to reset the value of the question.
        setValueExpression (str | None): Expression to decide on the value of the question to be set. Requires `setValueIf`.
        setValueIf (str | None): Expression with a condition to set the value of the question. Requires `setValueExpression`.
        showCommentArea (bool): Whether to show the comment area. Doesn't work with `showOtherItem`.
        showOtherItem (bool): Whether to show the 'Other' item. Doesn't work with `showCommentArea`.
        startWithNewLine (bool): Whether to start the question on a new line.
        state (str | None): If the question should be collapsed or expanded. Can be 'default', 'collapsed', 'expanded'.
        swapOrder (bool): Whether to swap the default (no, yes) order of the labels.
        titleLocation (str): The location of the title. Can be 'default', 'top', 'bottom', 'left', 'hidden'.
        useDisplayValuesInDynamicTexts (bool): Whether to use display names for question values in placeholders.
        validators (ValidatorModel | list[ValidatorModel] | None): Validator(s) for the question.
        valueFalse (str): Value for the 'false' option.
        valueTrue (str): Value for the 'true' option.
        visible (bool): Whether the question is visible.
        visibleIf (str | None): Expression to make the question visible.
        width (str): Width of the question in CSS units.
        addCode (dict | None): Additional code for the question. Usually not necessary.
        customCode (str | None): Custom JS commands to be added to the survey.
        customFunctions (str | None): Custom JS functions definitions to be added to the survey. To be used with `customCode`.
    """
    args = {
        "titleLocation": titleLocation,
        "description": description,
        "descriptionLocation": descriptionLocation,
        "isRequired": isRequired,
        "readOnly": readOnly,
        "visible": visible,
        "requiredIf": requiredIf,
        "enableIf": enableIf,
        "visibleIf": visibleIf,
        "validators": validators,
        "showOtherItem": showOtherItem,
        "showCommentArea": showCommentArea,
        "commentPlaceholder": commentPlaceholder,
        "commentText": commentText,
        "correctAnswer": correctAnswer,
        "defaultValue": defaultValue,
        "defaultValueExpression": defaultValueExpression,
        "requiredErrorText": requiredErrorText,
        "errorLocation": errorLocation,
        "hideNumber": hideNumber,
        "id": id,
        "maxWidth": maxWidth,
        "minWidth": minWidth,
        "resetValueIf": resetValueIf,
        "setValueIf": setValueIf,
        "setValueExpression": setValueExpression,
        "startWithNewLine": startWithNewLine,
        "state": state,
        "useDisplayValuesInDynamicTexts": useDisplayValuesInDynamicTexts,
        "width": width,
        "addCode": addCode,
        "labelFalse": labelFalse,
        "labelTrue": labelTrue,
        "swapOrder": swapOrder,
        "valueFalse": valueFalse,
        "valueTrue": valueTrue,
    }
    title = flatten(title)
    if len(title) != 1:
        return [
            QuestionBooleanModel(name=f"{name}_{i+1}", title=t, **args, **kwargs)
            for i, t in enumerate(title)
        ]
    return QuestionBooleanModel(name=name, title=title[0], **args, **kwargs)


def info(
    name: str,
    *infoHTML: str | list[str],
    titleLocation: str = "default",
    description: str | None = None,
    descriptionLocation: str = "default",
    isRequired: bool = False,
    readOnly: bool = False,
    visible: bool = True,
    requiredIf: str | None = None,
    enableIf: str | None = None,
    visibleIf: str | None = None,
    validators: ValidatorModel | list[ValidatorModel] | None = None,
    showOtherItem: bool = False,
    showCommentArea: bool = False,
    commentPlaceholder: str | None = None,
    commentText: str | None = None,
    correctAnswer: str | None = None,
    defaultValue: str | None = None,
    defaultValueExpression: str | None = None,
    requiredErrorText: str | None = None,
    errorLocation: str = "default",
    hideNumber: bool = False,
    id: str | None = None,
    maxWidth: str = "100%",
    minWidth: str = "300px",
    resetValueIf: str | None = None,
    setValueIf: str | None = None,
    setValueExpression: str | None = None,
    startWithNewLine: bool = True,
    state: str = "default",
    useDisplayValuesInDynamicTexts: bool = True,
    width: str = "",
    addCode: dict | None = None,
    **kwargs,
) -> QuestionHtmlModel | list[QuestionHtmlModel]:
    """Create an informational text object

    Args:
        name (str): The label of the question.
        infoHTML (str): The HTML content of the infobox.
        commentPlaceholder (str | None): Placeholder text for the comment area.
        commentText (str | None): Text for the comment area.
        correctAnswer (str | None): Correct answer for the question. Use for quizzes.
        defaultValue (str | None): Default value for the question.
        defaultValueExpression (str | None): Expression deciding the default value for the question.
        description (str | None): Optional subtitle or description of the question.
        descriptionLocation (str): The location of the description. Can be 'default', 'underTitle', 'underInput'.
        enableIf (str | None): Expression to enable the question.
        errorLocation (str | None): Location of the error text. Can be 'default' 'top', 'bottom'.
        hideNumber (bool): Whether to hide the question number.
        id (str | None): HTML id attribute for the question. Usually not necessary.
        maxWidth (str): Maximum width of the question in CSS units.
        minWidth (str): Minimum width of the question in CSS units.
        readOnly (bool): Whether the question is read-only.
        isRequired (bool): Whether the question is required.
        requiredErrorText (str | None): Error text if the required condition is not met.
        requiredIf (str | None): Expression to make the question required.
        resetValueIf (str | None): Expression to reset the value of the question.
        setValueExpression (str | None): Expression to decide on the value of the question to be set. Requires `setValueIf`.
        setValueIf (str | None): Expression with a condition to set the value of the question. Requires `setValueExpression`.
        showCommentArea (bool): Whether to show the comment area. Doesn't work with `showOtherItem`.
        showOtherItem (bool): Whether to show the 'Other' item. Doesn't work with `showCommentArea`.
        startWithNewLine (bool): Whether to start the question on a new line.
        state (str | None): If the question should be collapsed or expanded. Can be 'default', 'collapsed', 'expanded'.
        title (str | None): The visible title of the question. If None, `name` is used.
        titleLocation (str): The location of the title. Can be 'default', 'top', 'bottom', 'left', 'hidden'.
        useDisplayValuesInDynamicTexts (bool): Whether to use display names for question values in placeholders.
        validators (ValidatorModel | list[ValidatorModel] | None): Validator(s) for the question.
        visible (bool): Whether the question is visible.
        visibleIf (str | None): Expression to make the question visible.
        width (str): Width of the question in CSS units.
    addCode (dict | None): Additional code for the question. Usually not necessary.
        customCode (str | None): Custom JS commands to be added to the survey.
        customFunctions (str | None): Custom JS functions definitions to be added to the survey. To be used with `customCode`.
    """
    args = {
        "titleLocation": titleLocation,
        "description": description,
        "descriptionLocation": descriptionLocation,
        "isRequired": isRequired,
        "readOnly": readOnly,
        "visible": visible,
        "requiredIf": requiredIf,
        "enableIf": enableIf,
        "visibleIf": visibleIf,
        "validators": validators,
        "showOtherItem": showOtherItem,
        "showCommentArea": showCommentArea,
        "commentPlaceholder": commentPlaceholder,
        "commentText": commentText,
        "correctAnswer": correctAnswer,
        "defaultValue": defaultValue,
        "defaultValueExpression": defaultValueExpression,
        "requiredErrorText": requiredErrorText,
        "errorLocation": errorLocation,
        "hideNumber": hideNumber,
        "id": id,
        "maxWidth": maxWidth,
        "minWidth": minWidth,
        "resetValueIf": resetValueIf,
        "setValueIf": setValueIf,
        "setValueExpression": setValueExpression,
        "startWithNewLine": startWithNewLine,
        "state": state,
        "useDisplayValuesInDynamicTexts": useDisplayValuesInDynamicTexts,
        "width": width,
        "addCode": addCode,
    }
    infoHTML = flatten(infoHTML)
    if len(infoHTML) != 1:
        return [
            QuestionHtmlModel(name=f"{name}_{i+1}", html=html, **args, **kwargs)
            for i, html in enumerate(infoHTML)
        ]
    return QuestionHtmlModel(name=name, html=infoHTML[0], **args, **kwargs)


def matrix(
    name: str,
    title: str | list[str] | None,
    columns: list | dict,
    *rows: list | dict,
    alternateRows: bool | None = None,
    columnMinWidth: str | None = None,
    commentPlaceholder: str | None = None,
    commentText: str | None = None,
    correctAnswer: str | None = None,
    defaultValue: str | None = None,
    defaultValueExpression: str | None = None,
    description: str | None = None,
    descriptionLocation: str = "default",
    displayMode: str = "auto",
    eachRowUnique: bool | None = None,
    enableIf: str | None = None,
    errorLocation: str = "default",
    hideIfRowsEmpty: bool | None = None,
    hideNumber: bool = False,
    id: str | None = None,
    isAllRowRequired: bool = False,
    isRequired: bool = False,
    maxWidth: str = "100%",
    minWidth: str = "300px",
    readOnly: bool = False,
    requiredErrorText: str | None = None,
    requiredIf: str | None = None,
    resetValueIf: str | None = None,
    rowTitleWidth: str | None = None,
    rowsOrder: str = "initial",
    setValueExpression: str | None = None,
    setValueIf: str | None = None,
    showCommentArea: bool = False,
    showHeader: bool = True,
    showOtherItem: bool = False,
    startWithNewLine: bool = True,
    state: str = "default",
    titleLocation: str = "default",
    useDisplayValuesInDynamicTexts: bool = True,
    validators: ValidatorModel | list[ValidatorModel] | None = None,
    verticalAlign: str = "middle",
    visible: bool = True,
    visibleIf: str | None = None,
    width: str = "",
    addCode: dict | None = None,
    **kwargs,
) -> QuestionMatrixModel | list[QuestionMatrixModel]:
    """Create a matrix question object

    Attributes:
        name (str): The label of the question.
        title (str | None): The visible title of the question. If None, `name` is used.
        columns (list | dict): The columns of the matrix. Use primitives or dictionaries `{"text": ..., "value": ..., "otherParameter": ...}`.
        rows (list | dict): The rows of the matrix. Use primitives or dictionaries `{"text": ..., "value": ..., "otherParameter": ...}`.
        alternateRows (bool | None): Whether to alternate the rows.
        columnMinWidth (str | None): Minimum width of the column in CSS units.
        commentPlaceholder (str | None): Placeholder text for the comment area.
        commentText (str | None): Text for the comment area.
        correctAnswer (str | None): Correct answer for the question. Use for quizzes.
        defaultValue (str | None): Default value for the question.
        defaultValueExpression (str | None): Expression deciding the default value for the question.
        description (str | None): Optional subtitle or description of the question.
        descriptionLocation (str): The location of the description. Can be 'default', 'underTitle', 'underInput'.
        displayMode (str): The display mode of the matrix. Can be 'auto', 'list', 'table'.
        eachRowUnique (bool | None): Whether each row should have a unique answer. Defaults to False.
        enableIf (str | None): Expression to enable the question.
        errorLocation (str | None): Location of the error text. Can be 'default' 'top', 'bottom'.
        hideIfRowsEmpty (bool | None): Whether to hide the question if no rows are visible.
        hideNumber (bool): Whether to hide the question number.
        id (str | None): HTML id attribute for the question. Usually not necessary.
        isAllRowRequired (bool): Whether each and every row is to be required.
        maxWidth (str): Maximum width of the question in CSS units.
        minWidth (str): Minimum width of the question in CSS units.
        readOnly (bool): Whether the question is read-only.
        isRequired (bool): Whether the question is required.
        requiredErrorText (str | None): Error text if the required condition is not met.
        requiredIf (str | None): Expression to make the question required.
        resetValueIf (str | None): Expression to reset the value of the question.
        rowTitleWidth (str | None): Width of the row title in CSS units.
        rowsOrder (str): The order of the rows. Can be 'initial', 'random'.
        setValueExpression (str | None): Expression to decide on the value of the question to be set. Requires `setValueIf`.
        setValueIf (str | None): Expression with a condition to set the value of the question. Requires `setValueExpression`.
        showCommentArea (bool): Whether to show the comment area. Doesn't work with `showOtherItem`.
        showHeader (bool): Whether to show the header of the table.
        showOtherItem (bool): Whether to show the 'Other' item. Doesn't work with `showCommentArea`.
        startWithNewLine (bool): Whether to start the question on a new line.
        state (str | None): If the question should be collapsed or expanded. Can be 'default', 'collapsed', 'expanded'.
        titleLocation (str): The location of the title. Can be 'default', 'top', 'bottom', 'left', 'hidden'.
        useDisplayValuesInDynamicTexts (bool): Whether to use display names for question values in placeholders.
        validators (ValidatorModel | list[ValidatorModel] | None): Validator(s) for the question.
        verticalAlign (str): The vertical alignment of the content. Can be 'top', 'middle'.
        visible (bool): Whether the question is visible.
        visibleIf (str | None): Expression to make the question visible.
        width (str): Width of the question in CSS units.
        addCode (dict | None): Additional code for the question. Usually not necessary.
        customCode (str | None): Custom JS commands to be added to the survey.
        customFunctions (str | None): Custom JS functions definitions to be added to the survey. To be used with `customCode`.
    """
    args = {
        "titleLocation": titleLocation,
        "description": description,
        "descriptionLocation": descriptionLocation,
        "isRequired": isRequired,
        "readOnly": readOnly,
        "visible": visible,
        "requiredIf": requiredIf,
        "enableIf": enableIf,
        "visibleIf": visibleIf,
        "validators": validators,
        "showOtherItem": showOtherItem,
        "showCommentArea": showCommentArea,
        "commentPlaceholder": commentPlaceholder,
        "commentText": commentText,
        "correctAnswer": correctAnswer,
        "defaultValue": defaultValue,
        "defaultValueExpression": defaultValueExpression,
        "requiredErrorText": requiredErrorText,
        "errorLocation": errorLocation,
        "hideNumber": hideNumber,
        "id": id,
        "maxWidth": maxWidth,
        "minWidth": minWidth,
        "resetValueIf": resetValueIf,
        "setValueIf": setValueIf,
        "setValueExpression": setValueExpression,
        "startWithNewLine": startWithNewLine,
        "state": state,
        "useDisplayValuesInDynamicTexts": useDisplayValuesInDynamicTexts,
        "width": width,
        "addCode": addCode,
        "alternateRows": alternateRows,
        "columnMinWidth": columnMinWidth,
        "displayMode": displayMode,
        "rowTitleWidth": rowTitleWidth,
        "showHeader": showHeader,
        "verticalAlign": verticalAlign,
        "eachRowUnique": eachRowUnique,
        "hideIfRowsEmpty": hideIfRowsEmpty,
        "isAllRowRequired": isAllRowRequired,
        "rowsOrder": rowsOrder,
    }
    rows = flatten(rows)
    if not isinstance(title, list):
        title = [title]
    rows_changed = []
    for i, row in enumerate(rows):
        if isinstance(row, dict):
            rows_changed.append(row)
        else:
            rows_changed.append({"value": f"{name}_{i+1}", "text": row})
    if len(title) != 1:
        return [
            QuestionMatrixModel(
                name=f"{name}_{i+1}",
                title=t,
                columns=columns,
                rows=rows_changed,
                **args,
                **kwargs,
            )
            for i, t in enumerate(title)
        ]
    return QuestionMatrixModel(
        name=name, title=title[0], columns=columns, rows=rows_changed, **args, **kwargs
    )


def matrixDropdown(
    name: str,
    title: str | list[str],
    columns: list | QuestionModel | dict,
    *rows: list | dict,
    titleLocation: str = "default",
    description: str | None = None,
    descriptionLocation: str = "default",
    isRequired: bool = False,
    readOnly: bool = False,
    visible: bool = True,
    requiredIf: str | None = None,
    enableIf: str | None = None,
    visibleIf: str | None = None,
    validators: ValidatorModel | list[ValidatorModel] | None = None,
    showOtherItem: bool = False,
    showCommentArea: bool = False,
    commentPlaceholder: str | None = None,
    commentText: str | None = None,
    correctAnswer: str | None = None,
    defaultValue: str | None = None,
    defaultValueExpression: str | None = None,
    requiredErrorText: str | None = None,
    errorLocation: str = "default",
    hideNumber: bool = False,
    id: str | None = None,
    maxWidth: str = "100%",
    minWidth: str = "300px",
    resetValueIf: str | None = None,
    setValueIf: str | None = None,
    setValueExpression: str | None = None,
    startWithNewLine: bool = True,
    state: str = "default",
    useDisplayValuesInDynamicTexts: bool = True,
    width: str = "",
    addCode: dict | None = None,
    customCode: str | None = None,
    customFunctions: str | None = None,
    alternateRows: bool | None = None,
    columnMinWidth: str | None = None,
    displayMode: str = "auto",
    rowTitleWidth: str | None = None,
    showHeader: bool = True,
    verticalAlign: str = "middle",
    cellErrorLocation: str = "default",
    cellType: str | None = None,
    isUniqueCaseSensitive: bool = False,
    placeHolder: str | None = None,
    transposeData: bool = False,
    **kwargs,
):
    """Create a matrix, where each column can be a question of a specified type.

    Args:
        name (str): The label of the question.
        title (str | None): The visible title of the question. If None, `name` is used.
        columns (list | QuestionModel | dict): The columns of the matrix. Use question objects or dictionaries.
        rows (list | dict): The rows of the matrix. Use primitives or dictionaries `{"text": ..., "value": ..., "otherParameter": ...}`.
        alternateRows (bool | None): Whether to alternate the rows.
        cellErrorLocation (str): The location of the error text for the cells. Can be 'default', 'top', 'bottom'.
        cellType (str | None): The type of the matrix cells. Can be overridden for individual columns. Can be "dropdown" (default), "checkbox", "radiogroup", "tagbox", "text", "comment", "boolean", "expression", "rating".
        choices (str | dict | list | None): The default choices for all select questions. Can be overridden for individual columns. Can be string(s) or dictionary(-ies) with structure `{"value": ..., "text": ..., "otherParameter": ...}`.
        columnMinWidth (str | None): Minimum width of the column in CSS units.
        commentPlaceholder (str | None): Placeholder text for the comment area.
        commentText (str | None): Text for the comment area.
        correctAnswer (str | None): Correct answer for the question. Use for quizzes.
        defaultValue (str | None): Default value for the question.
        defaultValueExpression (str | None): Expression deciding the default value for the question.
        description (str | None): Optional subtitle or description of the question.
        descriptionLocation (str): The location of the description. Can be 'default', 'underTitle', 'underInput'.
        displayMode (str): The display mode of the matrix. Can be 'auto', 'list', 'table'.
        enableIf (str | None): Expression to enable the question.
        errorLocation (str | None): Location of the error text. Can be 'default' 'top', 'bottom'.
        hideNumber (bool): Whether to hide the question number.
        id (str | None): HTML id attribute for the question. Usually not necessary.
        isRequired (bool): Whether the question is required.
        isUniqueCaseSensitive (bool): Whether the case of the answer should be considered when checking for uniqueness. If `True`, "Kowalski" and "kowalski" will be considered different answers.
        maxWidth (str): Maximum width of the question in CSS units.
        minWidth (str): Minimum width of the question in CSS units.
        placeHolder (str | None): Placeholder text for the cells.
        readOnly (bool): Whether the question is read-only.
        requiredErrorText (str | None): Error text if the required condition is not met.
        requiredIf (str | None): Expression to make the question required.
        resetValueIf (str | None): Expression to reset the value of the question.
        rowTitleWidth (str | None): Width of the row title in CSS units.
        setValueExpression (str | None): Expression to decide on the value of the question to be set. Requires `setValueIf`.
        setValueIf (str | None): Expression with a condition to set the value of the question. Requires `setValueExpression`.
        showCommentArea (bool): Whether to show the comment area. Doesn't work with `showOtherItem`.
        showHeader (bool): Whether to show the header of the table.
        showOtherItem (bool): Whether to show the 'Other' item. Doesn't work with `showCommentArea`.
        startWithNewLine (bool): Whether to start the question on a new line.
        state (str | None): If the question should be collapsed or expanded. Can be 'default', 'collapsed', 'expanded'.
        titleLocation (str): The location of the title. Can be 'default', 'top', 'bottom', 'left', 'hidden'.
        transposeData (bool): Whether to show columns as rows. Default is False.
        useDisplayValuesInDynamicTexts (bool): Whether to use display names for question values in placeholders.
        validators (ValidatorModel | list[ValidatorModel] | None): Validator(s) for the question.
        verticalAlign (str): The vertical alignment of the content. Can be 'top', 'middle'.
        visible (bool): Whether the question is visible.
        visibleIf (str | None): Expression to make the question visible.
        width (str): Width of the question in CSS units.
        addCode (dict | None): Additional code for the question. Usually not necessary.
        customCode (str | None): Custom JS commands to be added to the survey.
        customFunctions (str | None): Custom JS functions definitions to be added to the survey. To be used with `customCode`.
    """
    args = {
        "titleLocation": titleLocation,
        "description": description,
        "descriptionLocation": descriptionLocation,
        "isRequired": isRequired,
        "readOnly": readOnly,
        "visible": visible,
        "requiredIf": requiredIf,
        "enableIf": enableIf,
        "visibleIf": visibleIf,
        "validators": validators,
        "showOtherItem": showOtherItem,
        "showCommentArea": showCommentArea,
        "commentPlaceholder": commentPlaceholder,
        "commentText": commentText,
        "correctAnswer": correctAnswer,
        "defaultValue": defaultValue,
        "defaultValueExpression": defaultValueExpression,
        "requiredErrorText": requiredErrorText,
        "errorLocation": errorLocation,
        "hideNumber": hideNumber,
        "id": id,
        "maxWidth": maxWidth,
        "minWidth": minWidth,
        "resetValueIf": resetValueIf,
        "setValueIf": setValueIf,
        "setValueExpression": setValueExpression,
        "startWithNewLine": startWithNewLine,
        "state": state,
        "useDisplayValuesInDynamicTexts": useDisplayValuesInDynamicTexts,
        "width": width,
        "addCode": addCode,
        "customCode": customCode,
        "customFunctions": customFunctions,
        "alternateRows": alternateRows,
        "columnMinWidth": columnMinWidth,
        "displayMode": displayMode,
        "rowTitleWidth": rowTitleWidth,
        "showHeader": showHeader,
        "verticalAlign": verticalAlign,
        "cellErrorLocation": cellErrorLocation,
        "cellType": cellType,
        "isUniqueCaseSensitive": isUniqueCaseSensitive,
        "placeHolder": placeHolder,
        "transposeData": transposeData,
    }
    rows = flatten(rows)
    if not isinstance(title, list):
        title = [title]
    if not isinstance(columns, list):
        columns = [columns]
    rows_changed = []
    for i, row in enumerate(rows):
        if isinstance(row, dict):
            rows_changed.append(row)
        else:
            rows_changed.append({"value": f"{name}_{i+1}", "text": row})
    if len(title) != 1:
        return [
            QuestionMatrixDropdownModel(
                name=f"{name}_{i+1}",
                title=t,
                columns=columns,
                rows=rows_changed,
                **args,
                **kwargs,
            )
            for i, t in enumerate(title)
        ]
    return QuestionMatrixDropdownModel(
        name=name, title=title[0], columns=columns, rows=rows_changed, **args, **kwargs
    )


def matrixDynamic(
    name: str,
    title: str | list[str] | None,
    *columns,
    titleLocation: str = "default",
    description: str | None = None,
    descriptionLocation: str = "default",
    isRequired: bool = False,
    readOnly: bool = False,
    visible: bool = True,
    requiredIf: str | None = None,
    enableIf: str | None = None,
    visibleIf: str | None = None,
    validators: ValidatorModel | list[ValidatorModel] | None = None,
    showOtherItem: bool = False,
    showCommentArea: bool = False,
    commentPlaceholder: str | None = None,
    commentText: str | None = None,
    correctAnswer: str | None = None,
    defaultValue: str | None = None,
    defaultValueExpression: str | None = None,
    requiredErrorText: str | None = None,
    errorLocation: str = "default",
    hideNumber: bool = False,
    id: str | None = None,
    maxWidth: str = "100%",
    minWidth: str = "300px",
    resetValueIf: str | None = None,
    setValueIf: str | None = None,
    setValueExpression: str | None = None,
    startWithNewLine: bool = True,
    state: str = "default",
    useDisplayValuesInDynamicTexts: bool = True,
    width: str = "",
    addCode: dict | None = None,
    rows: list | dict | None = None,
    alternateRows: bool | None = None,
    columnMinWidth: str | None = None,
    displayMode: str = "auto",
    rowTitleWidth: str | None = None,
    showHeader: bool = True,
    verticalAlign: str = "middle",
    cellErrorLocation: str = "default",
    cellType: str | None = None,
    isUniqueCaseSensitive: bool = False,
    placeHolder: str | None = None,
    transposeData: bool = False,
    addRowLocation: str = "default",
    addRowText: str | None = None,
    allowAddRows: bool = True,
    allowRemoveRows: bool = True,
    allowRowsDragAndDrop: bool = False,
    confirmDelete: bool = False,
    confirmDeleteText: str | None = None,
    defaultRowValue: str | None = None,
    defaultValueFromLastRow: bool = False,
    emptyRowsText: str | None = None,
    hideColumnsIfEmpty: bool = False,
    maxRowCount: int = 1000,
    minRowCount: int = 0,
    removeRowText: str | None = None,
    rowCount: int = 2,
    **kwargs,
) -> QuestionMatrixDynamicModel | list[QuestionMatrixDynamicModel]:
    """Create a dynamic matrix question object

    Attributes:
        name (str): The label of the question.
        title (str | None): The visible title of the question. If None, `name` is used.
        columns (list | dict): The columns of the matrix. Use primitives or dictionaries `{"text": ..., "value": ..., "type": ..., "otherParameter": ...}`.
        rows (list | dict): The rows of the matrix. Use primitives or dictionaries `{"text": ..., "value": ..., "otherParameter": ...}`.
        addRowLocation (str): The location of the 'Add row' button. Can be 'default', 'top', 'bottom', 'topBottom' (both top and bottom).
        addRowText (str | None): Text for the 'Add row' button.
        allowAddRows (bool): Whether to allow adding rows.
        allowRemoveRows (bool): Whether to allow removing rows.
        allowRowsDragAndDrop (bool): Whether to allow dragging and dropping rows to change order.
        alternateRows (bool | None): Whether to alternate the rows.
        cellErrorLocation (str): The location of the error text for the cells. Can be 'default', 'top', 'bottom'.
        cellType (str | None): The type of the matrix cells. Can be overridden for individual columns. Can be "dropdown" (default), "checkbox", "radiogroup", "tagbox", "text", "comment", "boolean", "expression", "rating".
        choices (str | dict | list): The default choices for all select questions. Can be overridden for individual columns. Can be string(s) or dictionary(-ies) with structure `{"value": ..., "text": ..., "otherParameter": ...}`.
        columnMinWidth (str | None): Minimum width of the column in CSS units.
        columns (list | dict): The columns of the matrix. Use primitives or dictionaries `{"text": ..., "value": ..., "type": ..., "otherParameter": ...}`.
        commentPlaceholder (str | None): Placeholder text for the comment area.
        commentText (str | None): Text for the comment area.
        confirmDelete (bool): Whether to prompt for confirmation before deleting a row. Default is False.
        confirmDeleteText (str | None): Text for the confirmation dialog when `confirmDelete` is True.
        correctAnswer (str | None): Correct answer for the question. Use for quizzes.
        defaultRowValue (str | None): Default value for the new rows that has no `defaultValue` property.
        defaultValue (str | None): Default value for the question.
        defaultValueExpression (str | None): Expression deciding the default value for the question.
        defaultValueFromLastRow (bool): Whether to copy the value from the last row to the new row.
        description (str | None): Optional subtitle or description of the question.
        descriptionLocation (str): The location of the description. Can be 'default', 'underTitle', 'underInput'.
        displayMode (str): The display mode of the matrix. Can be 'auto', 'list', 'table'.
        emptyRowsText (str | None): Text to display when there are no rows if `hideColumnsIfEmpty` is True.
        enableIf (str | None): Expression to enable the question.
        errorLocation (str | None): Location of the error text. Can be 'default' 'top', 'bottom'.
        hideColumnsIfEmpty (bool): Whether to hide columns if there are no rows.
        hideNumber (bool): Whether to hide the question number.
        id (str | None): HTML id attribute for the question. Usually not necessary.
        isUniqueCaseSensitive (bool): Whether the case of the answer should be considered when checking for uniqueness. If `True`, "Kowalski" and "kowalski" will be considered different answers.
        maxRowCount (int): Maximum number of rows.
        maxWidth (str): Maximum width of the question in CSS units.
        minRowCount (int): Minimum number of rows.
        minWidth (str): Minimum width of the question in CSS units.
        placeHolder (str | None): Placeholder text for the cells.
        readOnly (bool): Whether the question is read-only.
        removeRowText (str | None): Text for the 'Remove row' button.
        isRequired (bool): Whether the question is required.
        requiredErrorText (str | None): Error text if the required condition is not met.
        requiredIf (str | None): Expression to make the question required.
        resetValueIf (str | None): Expression to reset the value of the question.
        rowCount (int): The initial number of rows.
        rowTitleWidth (str | None): Width of the row title in CSS units.
        rows (list | dict): The rows of the matrix. Use primitives or dictionaries `{"text": ..., "value": ...}`.
        setValueExpression (str | None): Expression to decide on the value of the question to be set. Requires `setValueIf`.
        setValueIf (str | None): Expression with a condition to set the value of the question. Requires `setValueExpression`.
        showCommentArea (bool): Whether to show the comment area. Doesn't work with `showOtherItem`.
        showHeader (bool): Whether to show the header of the table.
        showOtherItem (bool): Whether to show the 'Other' item. Doesn't work with `showCommentArea`.
        startWithNewLine (bool): Whether to start the question on a new line.
        state (str | None): If the question should be collapsed or expanded. Can be 'default', 'collapsed', 'expanded'.
        titleLocation (str): The location of the title. Can be 'default', 'top', 'bottom', 'left', 'hidden'.
        transposeData (bool): Whether to show columns as rows. Default is False.
        useDisplayValuesInDynamicTexts (bool): Whether to use display names for question values in placeholders.
        validators (ValidatorModel | list[ValidatorModel] | None): Validator(s) for the question.
        verticalAlign (str): The vertical alignment of the content. Can be 'top', 'middle'.
        visible (bool): Whether the question is visible.
        visibleIf (str | None): Expression to make the question visible.
        width (str): Width of the question in CSS units.
        addCode (dict | None): Additional code for the question. Usually not necessary.
        customCode (str | None): Custom JS commands to be added to the survey.
        customFunctions (str | None): Custom JS functions definitions to be added to the survey. To be used with `customCode`.
    """
    args = {
        "titleLocation": titleLocation,
        "description": description,
        "descriptionLocation": descriptionLocation,
        "isRequired": isRequired,
        "readOnly": readOnly,
        "visible": visible,
        "requiredIf": requiredIf,
        "enableIf": enableIf,
        "visibleIf": visibleIf,
        "validators": validators,
        "showOtherItem": showOtherItem,
        "showCommentArea": showCommentArea,
        "commentPlaceholder": commentPlaceholder,
        "commentText": commentText,
        "correctAnswer": correctAnswer,
        "defaultValue": defaultValue,
        "defaultValueExpression": defaultValueExpression,
        "requiredErrorText": requiredErrorText,
        "errorLocation": errorLocation,
        "hideNumber": hideNumber,
        "id": id,
        "maxWidth": maxWidth,
        "minWidth": minWidth,
        "resetValueIf": resetValueIf,
        "setValueIf": setValueIf,
        "setValueExpression": setValueExpression,
        "startWithNewLine": startWithNewLine,
        "state": state,
        "useDisplayValuesInDynamicTexts": useDisplayValuesInDynamicTexts,
        "width": width,
        "addCode": addCode,
        "rows": rows,
        "alternateRows": alternateRows,
        "columnMinWidth": columnMinWidth,
        "displayMode": displayMode,
        "rowTitleWidth": rowTitleWidth,
        "showHeader": showHeader,
        "verticalAlign": verticalAlign,
        "cellErrorLocation": cellErrorLocation,
        "cellType": cellType,
        "isUniqueCaseSensitive": isUniqueCaseSensitive,
        "placeHolder": placeHolder,
        "transposeData": transposeData,
        "addRowLocation": addRowLocation,
        "addRowText": addRowText,
        "allowAddRows": allowAddRows,
        "allowRemoveRows": allowRemoveRows,
        "allowRowsDragAndDrop": allowRowsDragAndDrop,
        "confirmDelete": confirmDelete,
        "confirmDeleteText": confirmDeleteText,
        "defaultRowValue": defaultRowValue,
        "defaultValueFromLastRow": defaultValueFromLastRow,
        "emptyRowsText": emptyRowsText,
        "hideColumnsIfEmpty": hideColumnsIfEmpty,
        "maxRowCount": maxRowCount,
        "minRowCount": minRowCount,
        "removeRowText": removeRowText,
        "rowCount": rowCount,
    }
    columns = flatten(columns)
    if not isinstance(title, list):
        title = [title]
    if len(title) != 1:
        return [
            QuestionMatrixDynamicModel(
                name=f"{name}_{i+1}", title=t, columns=columns, **args, **kwargs
            )
            for i, t in enumerate(title)
        ]
    return QuestionMatrixDynamicModel(
        name=name, title=title[0], columns=columns, **args, **kwargs
    )


def slider(
    name: str,
    *title: str | list[str] | None,
    titleLocation: str = "default",
    description: str | None = None,
    descriptionLocation: str = "default",
    isRequired: bool = False,
    readOnly: bool = False,
    visible: bool = True,
    requiredIf: str | None = None,
    enableIf: str | None = None,
    visibleIf: str | None = None,
    validators: ValidatorModel | list[ValidatorModel] | None = None,
    showOtherItem: bool = False,
    showCommentArea: bool = False,
    commentPlaceholder: str | None = None,
    commentText: str | None = None,
    correctAnswer: str | None = None,
    defaultValue: str | None = None,
    defaultValueExpression: str | None = None,
    requiredErrorText: str | None = None,
    errorLocation: str = "default",
    hideNumber: bool = False,
    id: str | None = None,
    maxWidth: str = "100%",
    minWidth: str = "300px",
    resetValueIf: str | None = None,
    setValueIf: str | None = None,
    setValueExpression: str | None = None,
    startWithNewLine: bool = True,
    state: str = "default",
    useDisplayValuesInDynamicTexts: bool = True,
    width: str = "",
    addCode: dict | None = None,
    step: int = 1,
    rangeMin: int = 0,
    rangeMax: int = 100,
    pipsMode: str = "positions",
    pipsValues: list = [0, 25, 50, 75, 100],
    pipsText: list = [0, 25, 50, 75, 100],
    pipsDensity: int = 5,
    orientation: str = "horizontal",
    direction: str = "ltr",
    tooltips: bool = True,
    **kwargs,
) -> QuestionNoUiSliderModel | list[QuestionNoUiSliderModel]:
    """Create a slider question object

    Args:
        name (str): The label of the question.
        title (str | None): The visible title of the question. If None, `name` is used.
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
        addCode (dict | None): Additional code for the question. Usually not necessary.
        customCode (str | None): Custom JS commands to be added to the survey.
        customFunctions (str | None): Custom JS functions definitions to be added to the survey. To be used with `customCode`.
    """
    args = {
        "titleLocation": titleLocation,
        "description": description,
        "descriptionLocation": descriptionLocation,
        "isRequired": isRequired,
        "readOnly": readOnly,
        "visible": visible,
        "requiredIf": requiredIf,
        "enableIf": enableIf,
        "visibleIf": visibleIf,
        "validators": validators,
        "showOtherItem": showOtherItem,
        "showCommentArea": showCommentArea,
        "commentPlaceholder": commentPlaceholder,
        "commentText": commentText,
        "correctAnswer": correctAnswer,
        "defaultValue": defaultValue,
        "defaultValueExpression": defaultValueExpression,
        "requiredErrorText": requiredErrorText,
        "errorLocation": errorLocation,
        "hideNumber": hideNumber,
        "id": id,
        "maxWidth": maxWidth,
        "minWidth": minWidth,
        "resetValueIf": resetValueIf,
        "setValueIf": setValueIf,
        "setValueExpression": setValueExpression,
        "startWithNewLine": startWithNewLine,
        "state": state,
        "useDisplayValuesInDynamicTexts": useDisplayValuesInDynamicTexts,
        "width": width,
        "addCode": addCode,
        "step": step,
        "rangeMin": rangeMin,
        "rangeMax": rangeMax,
        "pipsMode": pipsMode,
        "pipsValues": pipsValues,
        "pipsText": pipsText,
        "pipsDensity": pipsDensity,
        "orientation": orientation,
        "direction": direction,
        "tooltips": tooltips,
    }
    title = flatten(title)
    if len(title) != 1:
        return [
            QuestionNoUiSliderModel(name=f"{name}_{i+1}", title=t, **args, **kwargs)
            for i, t in enumerate(title)
        ]
    return QuestionNoUiSliderModel(name=name, title=title[0], **args, **kwargs)


def image(
    name: str,
    *imageLink: str,
    titleLocation: str = "default",
    description: str | None = None,
    descriptionLocation: str = "default",
    isRequired: bool = False,
    readOnly: bool = False,
    visible: bool = True,
    requiredIf: str | None = None,
    enableIf: str | None = None,
    visibleIf: str | None = None,
    validators: ValidatorModel | list[ValidatorModel] | None = None,
    showOtherItem: bool = False,
    showCommentArea: bool = False,
    commentPlaceholder: str | None = None,
    commentText: str | None = None,
    correctAnswer: str | None = None,
    defaultValue: str | None = None,
    defaultValueExpression: str | None = None,
    requiredErrorText: str | None = None,
    errorLocation: str = "default",
    hideNumber: bool = False,
    id: str | None = None,
    maxWidth: str = "100%",
    minWidth: str = "300px",
    resetValueIf: str | None = None,
    setValueIf: str | None = None,
    setValueExpression: str | None = None,
    startWithNewLine: bool = True,
    state: str = "default",
    useDisplayValuesInDynamicTexts: bool = True,
    width: str = "",
    addCode: dict | None = None,
    altText: str | None = None,
    contentMode: str = "auto",
    imageFit: str = "contain",
    imageHeight: int | str = 150,
    imageWidth: int | str = 200,
    **kwargs,
) -> QuestionImageModel | list[QuestionImageModel]:
    """An image or video question object

    Args:
        name (str): The label of the question.
        imageLink (str | None): The src property for <img> or video link.
        altText (str | None): The alt property for <img>.
        commentPlaceholder (str | None): Placeholder text for the comment area.
        commentText (str | None): Text for the comment area.
        contentMode (str): The content type. Can be 'auto' (default), 'image', 'video', 'youtube'.
        correctAnswer (str | None): Correct answer for the question. Use for quizzes.
        defaultValue (str | None): Default value for the question.
        defaultValueExpression (str | None): Expression deciding the default value for the question.
        description (str | None): Optional subtitle or description of the question.
        descriptionLocation (str): The location of the description. Can be 'default', 'underTitle', 'underInput'.
        enableIf (str | None): Expression to enable the question.
        errorLocation (str | None): Location of the error text. Can be 'default' 'top', 'bottom'.
        hideNumber (bool): Whether to hide the question number.
        id (str | None): HTML id attribute for the question. Usually not necessary.
        imageFit (str): The object-fit property of <img>. Can be 'contain', 'cover', 'fill', 'none'. See MDN <https://developer.mozilla.org/en-US/docs/Web/CSS/object-fit>.
        imageHeight (int | str): The height of the image container in CSS units. See `imageFit`.
        imageWidth (int | str): The width of the image container in CSS units. See `imageFit`.
        isRequired (bool): Whether the question is required.
        maxWidth (str): Maximum width of the question in CSS units.
        minWidth (str): Minimum width of the question in CSS units.
        readOnly (bool): Whether the question is read-only.
        requiredErrorText (str | None): Error text if the required condition is not met.
        requiredIf (str | None): Expression to make the question required.
        resetValueIf (str | None): Expression to reset the value of the question.
        setValueExpression (str | None): Expression to decide on the value of the question to be set. Requires `setValueIf`.
        setValueIf (str | None): Expression with a condition to set the value of the question. Requires `setValueExpression`.
        showCommentArea (bool): Whether to show the comment area. Doesn't work with `showOtherItem`.
        showOtherItem (bool): Whether to show the 'Other' item. Doesn't work with `showCommentArea`.
        startWithNewLine (bool): Whether to start the question on a new line.
        state (str | None): If the question should be collapsed or expanded. Can be 'default', 'collapsed', 'expanded'.
        title (str | None): The visible title of the question. If None, `name` is used.
        titleLocation (str): The location of the title. Can be 'default', 'top', 'bottom', 'left', 'hidden'.
        useDisplayValuesInDynamicTexts (bool): Whether to use display names for question values in placeholders.
        validators (ValidatorModel | list[ValidatorModel] | None): Validator(s) for the question.
        visible (bool): Whether the question is visible.
        visibleIf (str | None): Expression to make the question visible.
        width (str): Width of the question in CSS units.
        addCode (dict | None): Additional code for the question. Usually not necessary.
        customCode (str | None): Custom JS commands to be added to the survey.
        customFunctions (str | None): Custom JS functions definitions to be added to the survey. To be used with `customCode`.
    """
    args = {
        "titleLocation": titleLocation,
        "description": description,
        "descriptionLocation": descriptionLocation,
        "isRequired": isRequired,
        "readOnly": readOnly,
        "visible": visible,
        "requiredIf": requiredIf,
        "enableIf": enableIf,
        "visibleIf": visibleIf,
        "validators": validators,
        "showOtherItem": showOtherItem,
        "showCommentArea": showCommentArea,
        "commentPlaceholder": commentPlaceholder,
        "commentText": commentText,
        "correctAnswer": correctAnswer,
        "defaultValue": defaultValue,
        "defaultValueExpression": defaultValueExpression,
        "requiredErrorText": requiredErrorText,
        "errorLocation": errorLocation,
        "hideNumber": hideNumber,
        "id": id,
        "maxWidth": maxWidth,
        "minWidth": minWidth,
        "resetValueIf": resetValueIf,
        "setValueIf": setValueIf,
        "setValueExpression": setValueExpression,
        "startWithNewLine": startWithNewLine,
        "state": state,
        "useDisplayValuesInDynamicTexts": useDisplayValuesInDynamicTexts,
        "width": width,
        "addCode": addCode,
        "altText": altText,
        "contentMode": contentMode,
        "imageFit": imageFit,
        "imageHeight": imageHeight,
        "imageWidth": imageWidth,
    }

    imageLink = flatten(imageLink)
    if len(imageLink) != 1:
        return [
            QuestionImageModel(
                name=f"{name}_{i+1}", imageLink=imageLink, **args, **kwargs
            )
            for i, imageLink in enumerate(imageLink)
        ]
    return QuestionImageModel(name=name, imageLink=imageLink[0], **args, **kwargs)


def consent(
    title: str = "Do you consent to take part in the study?",
    error: str = "You can't continue without a consent",
    mode: str = "forbid",
    name: str = "consent",
    **kwargs,
) -> QuestionBooleanModel:
    """Create a question with a consent to take part in the study

    Args:
        title (str): The visible title of the question. Defaults to "Do you consent to take part in the study?".
        error (str): Error shown if a person doesn't consent.
        mode (str): What to do if a person doesn't consent. Can be 'forbid' (default, doesn't allow to continue) or 'end' (redirects to the end).
            For 'end' to work, set `triggers` in the `survey()` call to `[{"type": "complete", "expression": "{consent} = false"}]`. You can also
            set `completedHtmlOnCondition` in the `survey()` call to `[{"expression": "{consent} = false", "html": "You can't continue without a consent"}]`
            to show a custom message in that case.
        name (str): The label of the question. Defaults to "consent".
        kwargs: Other arguments passed to `yesno()`.
    """
    if mode == "forbid":
        return yesno(
            name,
            title,
            validators=expressionValidator(
                expression=f"{{{name}}} = true", error=error
            ),
            isRequired=True,
            **kwargs,
        )
    elif mode == "end":
        return yesno(
            name,
            title,
            isRequired=True,
            **kwargs,
        )
    else:
        raise ValueError(f"Unknown mode: {mode}")
