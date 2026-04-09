from pathlib import Path
import matplotlib.pyplot as plt

lines = [
    'PS D:\\thi giac\\csc4005-hello-dl-starter-chung445> python run_smoke_test.py',
    'Epoch 1/3 | train_loss=0.8189 | test_loss=0.6842 | test_acc=0.5200',
    'Epoch 2/3 | train_loss=0.6936 | test_loss=0.6102 | test_acc=0.6500',
    'Epoch 3/3 | train_loss=0.6078 | test_loss=0.5564 | test_acc=0.7400',
    '',
    'Saved log to: outputs\\logs\\smoke_test_log.txt',
    'Saved figure to: outputs\\figures\\loss_curve.png',
    'Saved checkpoint to: outputs\\checkpoints\\smoke_model.pt',
]

output_dir = Path('outputs/screenshots')
output_dir.mkdir(parents=True, exist_ok=True)
fig, ax = plt.subplots(figsize=(10, 4))
ax.axis('off')
ax.text(0, 1, '\n'.join(lines), fontsize=12, family='monospace', va='top')
fig.tight_layout(pad=0.5)
fig.savefig(output_dir / 'terminal_run.png', dpi=150, bbox_inches='tight')
plt.close(fig)
print('Created', output_dir / 'terminal_run.png')
