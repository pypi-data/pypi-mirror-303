"use strict";
(self["webpackChunkm269_marking_plugin"] = self["webpackChunkm269_marking_plugin"] || []).push([["lib_index_js"],{

/***/ "./lib/index.js":
/*!**********************!*\
  !*** ./lib/index.js ***!
  \**********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/notebook */ "webpack/sharing/consume/default/@jupyterlab/notebook");
/* harmony import */ var _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _jupyterlab_cells__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/cells */ "webpack/sharing/consume/default/@jupyterlab/cells");
/* harmony import */ var _jupyterlab_cells__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_cells__WEBPACK_IMPORTED_MODULE_2__);




//import { NotebookActions } from '@jupyterlab/notebook';
/**
 * Initialization data for the m269_marking_plugin extension.
 */
const prep_command = 'm269_marking_plugin:prep';
const finish_command = 'm269_marking_plugin:finish';
const colourise = 'm269_marking_plugin:colourise';
const plugin = {
    id: 'm269_marking_plugin:plugin',
    description: 'Marking plugin for the M269 Open University module',
    autoStart: true,
    requires: [_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.ICommandPalette],
    activate: (app, palette) => {
        //const { commands } = app;
        console.log('M269 Marking Plugin is activated!');
        app.commands.addCommand(prep_command, {
            label: 'M269 Prep for Marking',
            caption: 'M269 Prep for Marking',
            execute: (args) => {
                const currentWidget = app.shell.currentWidget;
                if (currentWidget instanceof _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_1__.NotebookPanel) {
                    // Duplicate the file
                    const oldName = currentWidget.context.path;
                    const newName = oldName.replace(/\.ipynb$/, '-UNMARKED.ipynb');
                    app.serviceManager.contents.copy(oldName, newName)
                        .then(() => {
                        console.log('Notebook copied successfully:', newName);
                        // Process the answer cells and insert markdown cells in sequence
                        processAnswerCells(app, currentWidget);
                    });
                }
            }
        });
        app.commands.addCommand(colourise, {
            label: 'M269 Colourise',
            caption: 'M269 Colourise',
            execute: (ags) => {
                console.log('Colourising');
                injectStylesIfNeeded();
                const currentWidget = app.shell.currentWidget;
                if (currentWidget instanceof _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_1__.NotebookPanel) {
                    const notebook = currentWidget.content;
                    const model = notebook.model;
                    var cells = model === null || model === void 0 ? void 0 : model.cells;
                    if (cells) {
                        for (let i = 0; i < cells.length; i++) {
                            const cell = cells.get(i);
                            // Get the corresponding cell widget
                            const cellWidget = notebook.widgets[i];
                            if (cell instanceof _jupyterlab_cells__WEBPACK_IMPORTED_MODULE_2__.CodeCellModel || cell instanceof _jupyterlab_cells__WEBPACK_IMPORTED_MODULE_2__.MarkdownCellModel) {
                                const metadata = cell.metadata ? { ...cell.metadata } : {};
                                if (metadata['TYPE'] === 'ANSWER' && cellWidget) {
                                    // Apply the class to the cell's DOM node
                                    cellWidget.node.classList.add('answercell');
                                    //console.log(`Applied "answercell" class to cell ${i}`);
                                }
                                if (metadata['TYPE'] === 'FEEDBACK' && cellWidget) {
                                    //Apply the class to the cell's DOM node
                                    cellWidget.node.classList.add('feedbackcell');
                                }
                                if (metadata['TYPE'] === 'GUIDANCE' && cellWidget) {
                                    //Apply the class to the cell's DOM node
                                    cellWidget.node.classList.add('guidancecell');
                                }
                            }
                        }
                    }
                }
            }
        });
        app.commands.addCommand(finish_command, {
            label: 'M269 Finish Marking',
            caption: 'M269 Finish Marking',
            execute: async (args) => {
                console.log('Finalising marking');
                const currentWidget = app.shell.currentWidget;
                if (currentWidget instanceof _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_1__.NotebookPanel) {
                    // loop through cells
                    const notebook = currentWidget.content;
                    const model = notebook.model;
                    var cells = model === null || model === void 0 ? void 0 : model.cells;
                    let questionPartsList = [];
                    let outOfList = [];
                    let marksList = [];
                    if (cells) {
                        for (let i = 0; i < cells.length; i++) {
                            const cell = cells.get(i);
                            // if hasmarks = true
                            // Get the corresponding cell widget
                            const cellWidget = notebook.widgets[i];
                            if (cell instanceof _jupyterlab_cells__WEBPACK_IMPORTED_MODULE_2__.CodeCellModel || cell instanceof _jupyterlab_cells__WEBPACK_IMPORTED_MODULE_2__.MarkdownCellModel) {
                                const metadata = cell.metadata ? { ...cell.metadata } : {};
                                if (metadata['HASMARKS'] === true && cellWidget) {
                                    console.log(metadata['QUESTION']);
                                    const question = metadata['QUESTION'];
                                    if (typeof question === 'string') {
                                        questionPartsList.push(question);
                                    }
                                    let m = cell.sharedModel.getSource().split('/');
                                    marksList.push(m[0]);
                                    outOfList.push(Number(m[1]));
                                    //console.log(cell.sharedModel.getSource());
                                }
                            }
                            // then add to list of marks
                        }
                    }
                    console.log(questionPartsList);
                    console.log(outOfList);
                    console.log(marksList);
                    if (marksList.includes('?')) {
                        alert('At least one mark is missing');
                    }
                    else {
                        // check if final cell is SUMMARY = true
                        const cell = cells === null || cells === void 0 ? void 0 : cells.get(cells.length - 1);
                        const notebook = currentWidget.content;
                        if (cells) {
                            notebook.activeCellIndex = cells.length - 1;
                            notebook.activate();
                            const metadata = (cell === null || cell === void 0 ? void 0 : cell.metadata) ? { ...cell.metadata } : {};
                            if (metadata['SUMMARY'] === true) {
                                // if so, delete it
                                alert('deleting!');
                                await app.commands.execute('notebook:delete-cell');
                            }
                        }
                        // insert final summary cell
                        // Set the active cell
                        if (cells) {
                            notebook.activeCellIndex = cells.length - 1;
                            notebook.activate();
                            let marksTotal = 0;
                            let outOfTotal = 0;
                            // Insert a new cell below and wait for the command to complete
                            await app.commands.execute('notebook:insert-cell-below');
                            await app.commands.execute('notebook:change-cell-to-markdown');
                            // print table of marks
                            const newCell = notebook.activeCell;
                            let table = "<b>Marks:</b><br>";
                            table += "<table>";
                            table += "<tr><td><b>Question</b></td><td><b>Marks</b></td><td><b>Out Of</b></td></tr>";
                            for (let i = 0; i < questionPartsList.length; i++) {
                                marksTotal += Number(marksList[i]);
                                outOfTotal += outOfList[i];
                                table += "<tr><td>" + questionPartsList[i] + "</td><td>" + marksList[i] + "</td><td>" + outOfList[i] + "</td></tr>";
                            }
                            table += "<tr><td><b>Total</b></td><td><b>" + marksTotal + "</b></td><td><b>" + outOfTotal + "</b></td></tr>";
                            table += "</table>";
                            newCell === null || newCell === void 0 ? void 0 : newCell.model.sharedModel.setSource(table);
                            newCell === null || newCell === void 0 ? void 0 : newCell.model.setMetadata('SUMMARY', true);
                            const sessionContext = currentWidget.context.sessionContext;
                            _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_1__.NotebookActions.run(notebook, sessionContext);
                        }
                    }
                }
            }
        });
        // Add the command to the command palette
        const category = 'M269';
        palette.addItem({ command: prep_command, category, args: { origin: 'from palette' } });
        palette.addItem({ command: colourise, category, args: { origin: 'from palette' } });
        palette.addItem({ command: finish_command, category, args: { origin: 'from palette' } });
    }
};
async function addFeedbackCell(cellNum, app, currentWidget) {
    const notebook = currentWidget.content;
    // Set the active cell
    notebook.activeCellIndex = cellNum;
    notebook.activate();
    // Insert a new cell below and wait for the command to complete
    await app.commands.execute('notebook:insert-cell-below');
    console.log('Feedback cell inserted');
    await app.commands.execute('notebook:change-cell-to-markdown');
    console.log('  Feedback cell changed to markdown successfully!');
    // Access the newly inserted cell and set the text
    const newCell = notebook.activeCell;
    if (newCell) {
        newCell.model.sharedModel.setSource("Feedback: ");
        console.log('  "Feedback" inserted');
        newCell.model.setMetadata('TYPE', 'FEEDBACK');
        console.log('  Metadata set');
    }
}
async function addMarksCell(cellNum, app, currentWidget, maxMarks, qp) {
    const notebook = currentWidget.content;
    // Set the active cell
    notebook.activeCellIndex = cellNum;
    notebook.activate();
    // Insert a new cell below and wait for the command to complete
    await app.commands.execute('notebook:insert-cell-below');
    console.log('Marks cell inserted');
    await app.commands.execute('notebook:change-cell-to-markdown');
    console.log('  Marks cell changed to markdown successfully!');
    // Access the newly inserted cell and set the text
    const newCell = notebook.activeCell;
    if (newCell) {
        newCell.model.sharedModel.setSource("?/" + (maxMarks.toString()));
        console.log('  ?/? inserted');
        newCell.model.setMetadata('TYPE', 'FEEDBACK');
        newCell.model.setMetadata('QUESTION', qp);
        newCell.model.setMetadata('HASMARKS', true);
        console.log('  Metadata set');
    }
}
async function processAnswerCells(app, currentWidget) {
    const notebook = currentWidget.content;
    const model = notebook.model;
    var cells = model === null || model === void 0 ? void 0 : model.cells;
    let questionCellList = [];
    let marksList = [];
    let questionNumbers = [];
    if (cells) {
        for (let i = 0; i < cells.length; i++) {
            const cell = cells.get(i);
            if (cell instanceof _jupyterlab_cells__WEBPACK_IMPORTED_MODULE_2__.CodeCellModel || cell instanceof _jupyterlab_cells__WEBPACK_IMPORTED_MODULE_2__.MarkdownCellModel) {
                const metadata = cell.metadata ? { ...cell.metadata } : {};
                if (metadata['TYPE'] === 'ANSWER') {
                    questionCellList.push(i);
                    if (typeof metadata['MARKS'] === 'number') {
                        marksList.push(metadata['MARKS']);
                    }
                    if (typeof metadata['QUESTION'] === 'string') {
                        questionNumbers.push(metadata['QUESTION']);
                    }
                }
            }
        }
    }
    else {
        console.error('No cells found in the notebook.');
    }
    questionCellList.reverse();
    marksList.reverse();
    questionNumbers.reverse();
    console.log(questionCellList);
    //  for (const value of questionCellList) {
    for (const [index, value] of questionCellList.entries()) {
        console.log(`Inserting after: ${value}`);
        await addMarksCell(value, app, currentWidget, marksList[index], questionNumbers[index]);
        console.log('Marks done, now Feedback.');
        await addFeedbackCell(value, app, currentWidget);
        console.log('Done');
        console.log();
    }
    await app.commands.execute(colourise);
}
function injectStylesIfNeeded() {
    const styleId = 'm269-css'; // A unique ID for the style element
    // Check if the style element already exists
    if (!document.getElementById(styleId)) {
        // If not, create and inject the CSS
        const style = document.createElement('style');
        style.id = styleId; // Assign the ID to the style element for future checks
        style.innerHTML = `
          .answercell{background-color: #ffffcc;}
          .feedbackcell{background-color: #8d9aa1;}
          .guidancecell{background-color: #f2c0d4;}
        `;
        document.head.appendChild(style);
        console.log('Custom CSS injected');
    }
    else {
        console.log('Custom CSS already exists');
    }
}
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (plugin);


/***/ })

}]);
//# sourceMappingURL=lib_index_js.9f2e5461ce1200a490ae.js.map