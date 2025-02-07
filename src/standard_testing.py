import torch
import numpy as np
from src.utils.testing_utils import save_batch_as_color_imgs 
from src.utils.testing_utils import save_tensor_as_color_img

def test_solver(solver, test_dataloader,
                 measurement_process, device='cpu'):

    #####################TEST##########################
    loss_accumulator = []
    mse_loss = torch.nn.MSELoss()
    for ii, sample_batch in enumerate(test_dataloader):
        sample_batch = sample_batch.to(device=device)
        y = measurement_process(sample_batch)
        initial_point = y

        reconstruction = solver(initial_point, iterations=6)

        reconstruction = torch.clamp(reconstruction, -1 ,1)

        loss = mse_loss(reconstruction, sample_batch)
        loss_logger = loss.cpu().detach().numpy()
        loss_accumulator.append(loss_logger)
        loss_value = loss.cpu().detach().numpy()
        logging_string = "Loss: " + str(loss_value)
        print(logging_string)

        save_tensor_as_color_img(sample_batch, "results/" + str(loss_value) + "_original.png")
        save_tensor_as_color_img(y, "results/" + str(loss_value) + "_in.png")
        save_tensor_as_color_img(reconstruction, "results/" + str(loss_value) + "_out.png")

        if ii > 6:
            exit()

    loss_array = np.asarray(loss_accumulator)
    loss_mse = np.mean(loss_array)
    PSNR = -10 * np.log10(loss_mse)
    percentiles = np.percentile(loss_array, [25,50,75])
    percentiles = -10.0*np.log10(percentiles)
    print("TEST LOSS: " + str(sum(loss_accumulator) / len(loss_accumulator)), flush=True)
    print("MEAN TEST PSNR: " + str(PSNR), flush=True)
    print("TEST PSNR QUARTILES AND MEDIAN: " + str(percentiles[0]) +
          ", " + str(percentiles[1]) + ", " + str(percentiles[2]), flush=True)
