# ISTI Predictor

## Training

- ``-e'``, ``epochs'``
    - Number of Epochs. Set to 50 by default.
-  ``- lr'``, ``learning_rate'``
	- Learning Rate. Set to 0.01 by default.
-  ``-ba'``, ``batch_size'``
	- Batch Size.
-  ``-seed``
	- Random seed. Set to 5 by default.
-  ``-data``
	- Data path. Will search for ``mat_files`` in ``../data/`` directory by default.
-  ``-label``
	- Label path. Will search for ``normalized_pep_labels`` in ``../data/`` directory by default.
-  ``-sync``
	- ECG & Video sync. Will search for ``sync_data`` in ``../data/`` directory by default.
-  ``-phase``
	- Run in Train/Test mode.
    - Can take on values "train", "test".
- ``split``
    - Specifies the training data and validation data split. Set to 0.8 by default.
- ``- min_batch`` '--frames_in_GPU'
    - Number of frames per batch from the video to go in the GPU.

It is possible to resume training through the following options/flags:

- ``-resume``
	- Resume training.
- ``-hyper_param'``
	- Use (?) existing hyper-parameters.
- ``cp``, ``--checkpoint_path``
    - Specify the path of the checkpoints, in order to resume training. Searches through ``../model_checkpoints_r50`` by default.
