import torch
import torch.nn as nn
import torch.nn.functional as F

#M1 아키텍쳐가 정의된 클래스
class TemporalFusionTransformer(nn.Module):
    def __init__(self, hidden_size, lstm_layers, dropout, output_size, attention_head_size, static_input_size, sequence_input_size):
        super(TemporalFusionTransformer, self).__init__()
        self.hidden_size = hidden_size
        self.lstm_layers = lstm_layers
        self.dropout = dropout
        self.output_size = output_size
        self.attention_head_size = attention_head_size
        
        self.static_vsn = VariableSelectionNetwork(static_input_size, hidden_size)
        self.sequence_vsn = VariableSelectionNetwork(sequence_input_size, hidden_size)
        
        self.lstm = nn.LSTM(input_size=sequence_input_size, hidden_size=hidden_size, num_layers=lstm_layers, dropout=dropout, batch_first=True)
        self.attention = nn.MultiheadAttention(embed_dim=hidden_size, num_heads=attention_head_size, batch_first=True)
        self.static_fc = nn.Linear(static_input_size, hidden_size)
        self.fc = nn.Linear(hidden_size * 2, output_size)
        self.sigmoid = nn.Sigmoid()
        
    def forward(self, x_static, x_sequence):
        static_weights = self.static_vsn(x_static)
        static_out = torch.mul(x_static, static_weights)
        static_out = self.static_fc(static_out)
        
        sequence_weights = self.sequence_vsn(x_sequence)
        x_sequence = torch.mul(x_sequence, sequence_weights)
        
        lstm_out, (h_n, c_n) = self.lstm(x_sequence.unsqueeze(1))
        attn_output, attn_output_weights = self.attention(lstm_out, lstm_out, lstm_out)
        
        combined_out = torch.cat((static_out, attn_output[:, -1, :]), dim=1)
        output = self.fc(combined_out)
        output = self.sigmoid(output)
        
        return output, static_weights, sequence_weights


class VariableSelectionNetwork(nn.Module):
    def __init__(self, input_size, hidden_size):
        super(VariableSelectionNetwork, self).__init__()
        self.grn = GatedResidualNetwork(input_size, hidden_size)
        self.softmax = nn.Softmax(dim=-1)

    def forward(self, x, context=None):
        x = self.grn(x, context)
        return self.softmax(x)


class GatedResidualNetwork(nn.Module):
    def __init__(self, input_size, hidden_size):
        super(GatedResidualNetwork, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.fc2 = nn.Linear(hidden_size, input_size)
        self.fc3 = nn.Linear(input_size, hidden_size)
        self.fc4 = nn.Linear(hidden_size, input_size)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x, context=None):
        if context is not None:
            x = torch.cat((x, context), dim=1)
        x1 = torch.relu(self.fc1(x))
        x1 = self.fc2(x1)
        x2 = torch.relu(self.fc3(x))
        x2 = self.fc4(x2)
        x2 = self.sigmoid(x2)
        return x1 * x2



# class TemporalFusionTransformer(nn.Module):
#     def __init__(self, hidden_size, lstm_layers, dropout, output_size, attention_head_size, static_input_size, sequence_input_size):
#         super(TemporalFusionTransformer, self).__init__()
#         self.hidden_size = hidden_size
#         self.lstm_layers = lstm_layers
#         self.dropout = dropout
#         self.output_size = output_size
#         self.attention_head_size = attention_head_size
        
#         self.static_vsn = VariableSelectionNetwork(static_input_size, hidden_size)
#         self.sequence_vsn = VariableSelectionNetwork(sequence_input_size, hidden_size)
        
#         self.lstm = nn.LSTM(input_size=sequence_input_size, hidden_size=hidden_size, num_layers=lstm_layers, dropout=dropout, batch_first=True)
#         self.attention = nn.MultiheadAttention(embed_dim=hidden_size, num_heads=attention_head_size, batch_first=True)
#         self.static_fc = nn.Linear(static_input_size, hidden_size)
#         self.fc = nn.Linear(hidden_size * 2, output_size)
#         self.sigmoid = nn.Sigmoid()
        
#     def forward(self, x_static, x_sequence):
#         static_weights = self.static_vsn(x_static)
#         static_out = torch.mul(x_static, static_weights)
#         static_out = self.static_fc(static_out)
        
#         sequence_weights = self.sequence_vsn(x_sequence)
#         x_sequence = torch.mul(x_sequence, sequence_weights)
        
#         lstm_out, (h_n, c_n) = self.lstm(x_sequence.unsqueeze(1))
#         attn_output, attn_output_weights = self.attention(lstm_out, lstm_out, lstm_out)
        
#         combined_out = torch.cat((static_out, attn_output[:, -1, :]), dim=1)
#         output = self.fc(combined_out)
#         output = self.sigmoid(output)
        
#         return output, static_weights, sequence_weights


# class VariableSelectionNetwork(nn.Module):
#     def __init__(self, input_size, hidden_size):
#         super(VariableSelectionNetwork, self).__init__()
#         self.grn = GatedResidualNetwork(input_size, hidden_size)
#         self.softmax = nn.Softmax(dim=-1)

#     def forward(self, x, context=None):
#         x = self.grn(x, context)
#         return self.softmax(x)



# class GatedResidualNetwork(nn.Module):
#     def __init__(self, input_size, hidden_size):
#         super(GatedResidualNetwork, self).__init__()
#         self.fc1 = nn.Linear(input_size, hidden_size)
#         self.fc2 = nn.Linear(hidden_size, input_size)
#         self.fc3 = nn.Linear(input_size, hidden_size)
#         self.fc4 = nn.Linear(hidden_size, input_size)
#         self.sigmoid = nn.Sigmoid()

#     def forward(self, x, context=None):
#         if context is not None:
#             x = torch.cat((x, context), dim=1)
#         x1 = torch.relu(self.fc1(x))
#         x1 = self.fc2(x1)
#         x2 = torch.relu(self.fc3(x))
#         x2 = self.fc4(x2)
#         x2 = self.sigmoid(x2)
#         return x1 * x2
