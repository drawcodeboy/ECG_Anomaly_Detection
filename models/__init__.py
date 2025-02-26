from .lstm_ae import LSTMAutoencoder
from .mae_loss import MAELoss

def load_model(model_name:str='LSTM-AE', 
               in_out_dim:int=1):
    
    if model_name == 'LSTM-AE':
        return LSTMAutoencoder(num_layers=5,
                               in_out_dim=in_out_dim,
                               hidden_dims=[128, 64, 32, 16, 8])
    
        
    elif model_name == 'ResLSTM-AE': # Residual LSTM Experiments
        return LSTMAutoencoder(num_layers=5,
                               in_out_dim=in_out_dim,
                               hidden_dims=[128, 64, 32, 16, 8],
                               encoder_lstm_type='res',
                               decoder_lstm_type='res')
        
    elif model_name == 'EnResLSTM-AE': # Residual LSTM Experiments
        return LSTMAutoencoder(num_layers=5,
                               in_out_dim=in_out_dim,
                               hidden_dims=[128, 64, 32, 16, 8],
                               encoder_lstm_type='res',
                               decoder_lstm_type='plain')
        
    elif model_name == 'DeResLSTM-AE':
        return LSTMAutoencoder(num_layers=5,
                               in_out_dim=in_out_dim,
                               hidden_dims=[128, 64, 32, 16, 8],
                               encoder_lstm_type='plain',
                               decoder_lstm_type='res')
        
    elif model_name == 'SparLSTM-AE':
        return LSTMAutoencoder(num_layers=5, 
                               in_out_dim=in_out_dim,
                               hidden_dims=[128, 64, 32, 16, 8],
                               sparsity_param=0.05,
                               sparsity_weight=1e-4)
        
    elif model_name == 'SparDeResLSTM-AE' or model_name == 'SRL-AE': # Proposed Model
        return LSTMAutoencoder(num_layers=5,
                               in_out_dim=in_out_dim,
                               hidden_dims=[128, 64, 32, 16, 8],
                               encoder_lstm_type='plain',
                               decoder_lstm_type='res',
                               sparsity_param=0.05,
                               sparsity_weight=1e-4)
        
    else:
        raise AssertionError(f"{model_name} is not supported.")