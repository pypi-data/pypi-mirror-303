import {
  JupyterFrontEnd,
  JupyterFrontEndPlugin
} from '@jupyterlab/application';
import { ICommandPalette } from '@jupyterlab/apputils';
import { NotebookPanel } from '@jupyterlab/notebook';
import { CodeCellModel, MarkdownCellModel } from '@jupyterlab/cells';
import { NotebookActions } from '@jupyterlab/notebook';

//import { NotebookActions } from '@jupyterlab/notebook';

/**
 * Initialization data for the m269_marking_plugin extension.
 */
const prep_command = 'm269_marking_plugin:prep';
const finish_command = 'm269_marking_plugin:finish'
const colourise = 'm269_marking_plugin:colourise';

const plugin: JupyterFrontEndPlugin<void> = {
  id: 'm269_marking_plugin:plugin',
  description: 'Marking plugin for the M269 Open University module',
  autoStart: true,
  requires: [ICommandPalette], // Inject the palette service
  activate: (app: JupyterFrontEnd, palette: ICommandPalette) => {
    //const { commands } = app;
    console.log('M269 Marking Plugin is activated!');

    app.commands.addCommand(prep_command, {
      label: 'M269 Prep for Marking',
      caption: 'M269 Prep for Marking',
      execute: (args: any) => {
        const currentWidget = app.shell.currentWidget;
        if (currentWidget instanceof NotebookPanel) {
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
      execute: (ags: any) => {
        console.log('Colourising');
        injectStylesIfNeeded();
        const currentWidget = app.shell.currentWidget;
        if (currentWidget instanceof NotebookPanel) {
          const notebook = currentWidget.content;
          const model = notebook.model;
          var cells = model?.cells;      
          if (cells) {
            for (let i = 0; i < cells.length; i++) {
              const cell = cells.get(i);
    
              // Get the corresponding cell widget
              const cellWidget = notebook.widgets[i]; 
    
              if (cell instanceof CodeCellModel || cell instanceof MarkdownCellModel) {
                const metadata = cell.metadata ? { ...cell.metadata } : {};
        
                if (metadata['TYPE'] === 'ANSWER' && cellWidget) {
                  // Apply the class to the cell's DOM node
                  cellWidget.node.classList.add('answercell');
                  //console.log(`Applied "answercell" class to cell ${i}`);
                }
                if (metadata['TYPE'] === 'FEEDBACK' && cellWidget) {
                  //Apply the class to the cell's DOM node
                  cellWidget.node.classList.add('feedbackcell')
                }
                if (metadata['TYPE'] === 'GUIDANCE' && cellWidget) {
                  //Apply the class to the cell's DOM node
                  cellWidget.node.classList.add('guidancecell')
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
      execute: async (args: any) => {
        console.log('Finalising marking');
        const currentWidget = app.shell.currentWidget;
        if (currentWidget instanceof NotebookPanel) {
          // loop through cells
          const notebook = currentWidget.content;
          const model = notebook.model;
          var cells = model?.cells;
          let questionPartsList: string[] = [];
          let outOfList: number[] = [];
          let marksList: string[] = [];
    
          if (cells) {
            for (let i = 0; i < cells.length; i++) {
              const cell = cells.get(i);
              // if hasmarks = true
              // Get the corresponding cell widget
              const cellWidget = notebook.widgets[i]; 

              if (cell instanceof CodeCellModel || cell instanceof MarkdownCellModel) {
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
          } else {
            // check if final cell is SUMMARY = true
            const cell = cells?.get(cells.length-1);
            const notebook = currentWidget.content;
            if (cells) {
              notebook.activeCellIndex = cells.length - 1;
              notebook.activate();  
              const metadata = cell?.metadata ? { ...cell.metadata } : {};
              if (metadata['SUMMARY'] === true) {
                // if so, delete it
                alert('deleting!');
                await app.commands.execute('notebook:delete-cell')
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
              await app.commands.execute('notebook:insert-cell-below')
              await app.commands.execute('notebook:change-cell-to-markdown');
              // print table of marks
              const newCell = notebook.activeCell;
              let table = "<b>Marks:</b><br>"
              table += "<table>";
              table += "<tr><td><b>Question</b></td><td><b>Marks</b></td><td><b>Out Of</b></td></tr>";
              for (let i = 0; i < questionPartsList.length; i++) {
                marksTotal += Number(marksList[i]);
                outOfTotal += outOfList[i];
                table += "<tr><td>"+questionPartsList[i]+"</td><td>"+marksList[i]+"</td><td>"+outOfList[i]+"</td></tr>";
              }
              table += "<tr><td><b>Total</b></td><td><b>"+marksTotal+"</b></td><td><b>"+outOfTotal+"</b></td></tr>";
              table += "</table>";
              newCell?.model.sharedModel.setSource(table);
              newCell?.model.setMetadata('SUMMARY', true);
              const sessionContext = currentWidget.context.sessionContext;
              NotebookActions.run(notebook, sessionContext);

            }          
          }
        }
      }
    });

    // Add the command to the command palette
    const category = 'M269';
    palette.addItem({ command: prep_command, category, args: { origin: 'from palette' } });
    palette.addItem({ command: colourise, category, args: { origin: 'from palette' } });
    palette.addItem({ command: finish_command, category, args: {origin: 'from palette' }});
  }
};

async function addFeedbackCell(cellNum: number, app: JupyterFrontEnd, currentWidget: NotebookPanel) {
  const notebook = currentWidget.content;

  // Set the active cell
  notebook.activeCellIndex = cellNum;
  notebook.activate();

  // Insert a new cell below and wait for the command to complete
  await app.commands.execute('notebook:insert-cell-below')
  console.log('Feedback cell inserted');
  await app.commands.execute('notebook:change-cell-to-markdown');
  console.log('  Feedback cell changed to markdown successfully!');
  // Access the newly inserted cell and set the text
  const newCell = notebook.activeCell;
  if (newCell) {
    newCell.model.sharedModel.setSource("Feedback: ");
    console.log('  "Feedback" inserted');
    newCell.model.setMetadata('TYPE','FEEDBACK');
    console.log('  Metadata set');
  }
}

async function addMarksCell(cellNum: number, app: JupyterFrontEnd, currentWidget: NotebookPanel, maxMarks: number, qp: string) {
  const notebook = currentWidget.content;

  // Set the active cell
  notebook.activeCellIndex = cellNum;
  notebook.activate();

  // Insert a new cell below and wait for the command to complete
  await app.commands.execute('notebook:insert-cell-below')
  console.log('Marks cell inserted');
  await app.commands.execute('notebook:change-cell-to-markdown');
  console.log('  Marks cell changed to markdown successfully!');
  // Access the newly inserted cell and set the text
  const newCell = notebook.activeCell;
  if (newCell) {
    newCell.model.sharedModel.setSource("?/"+(maxMarks.toString()));
      console.log('  ?/? inserted');
      newCell.model.setMetadata('TYPE','FEEDBACK');
      newCell.model.setMetadata('QUESTION', qp);
      newCell.model.setMetadata('HASMARKS',true);
      console.log('  Metadata set');
    }
}

async function processAnswerCells(app: JupyterFrontEnd, currentWidget: NotebookPanel) {
  const notebook = currentWidget.content;
  const model = notebook.model;
  var cells = model?.cells;
  let questionCellList: number[] = [];
  let marksList: number[] = []
  let questionNumbers: string[] = [];

  if (cells) {
    for (let i = 0; i < cells.length; i++) {
      const cell = cells.get(i);
      if (cell instanceof CodeCellModel || cell instanceof MarkdownCellModel) {
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
  } else {
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
  } else {
    console.log('Custom CSS already exists');
  }
}

export default plugin;