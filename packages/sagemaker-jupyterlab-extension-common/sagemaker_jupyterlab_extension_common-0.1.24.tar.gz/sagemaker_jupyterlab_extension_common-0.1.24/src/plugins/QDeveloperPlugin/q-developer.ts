import { JupyterFrontEnd, LabShell } from '@jupyterlab/application';
import { qIcon } from '../../components/icons';

export const JUPYTER_AI_CHAT_WIDGET_ID = 'jupyter-ai::chat';

export function updateSidebarIconToQ(app: JupyterFrontEnd): void {
  if (app.shell instanceof LabShell) {
    const widgets = Array.from(app.shell.widgets('left'));
    const chatWidget = widgets.find((widget) => widget.id === JUPYTER_AI_CHAT_WIDGET_ID);
    if (chatWidget) {
      chatWidget.title.icon = qIcon;
    }
  }
}
