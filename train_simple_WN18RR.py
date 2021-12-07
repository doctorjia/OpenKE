import openke
import sys
from openke.config import Trainer, Tester
from openke.module.model import SimplE
from openke.module.loss import SoftplusLoss
from openke.module.strategy import NegativeSampling
from openke.data import TrainDataLoader, TestDataLoader


# dataloader for training
def load_data(timestamp):
    train_dataloader = TrainDataLoader(
        in_path = "./benchmarks/archive_" + str(timestamp) + "/",
        nbatches = 100,
        threads = 8,
        sampling_mode = "normal",
        bern_flag = 1,
        filter_flag = 1,
        neg_ent = 25,
        neg_rel = 0
    )

    # dataloader for test
    test_dataloader = TestDataLoader("./benchmarks/archive_" + str(timestamp) + "/", "link")

    # define the model
    simple = SimplE(
        ent_tot = train_dataloader.get_ent_tot(),
        rel_tot = train_dataloader.get_rel_tot(),
        dim = 200
    )

    # define the loss function
    model = NegativeSampling(
        model = simple,
        loss = SoftplusLoss(),
        batch_size = train_dataloader.get_batch_size(),
        regul_rate = 1.0
    )

    return train_dataloader, test_dataloader, simple, model


# train the model
train_dataloader_0, test_dataloader_0, simple_0, model_0 = load_data(0)
trainer = Trainer(model = model_0, data_loader = train_dataloader_0, train_times = 500, alpha = 0.5, use_gpu = True,
                  opt_method = "adagrad")
trainer.run()
simple_0.save_checkpoint('./checkpoint/simple_0.ckpt')
simple_0.save_parameters('./parameters/simple_0.json')
simple_0.load_checkpoint('./checkpoint/simple_0.ckpt')
tester = Tester(model = simple_0, data_loader = test_dataloader_0, use_gpu = True)
tester.run_link_prediction(type_constrain = False)

for i in range(5):
    train_dataloader_now, test_dataloader_now, simple_now, model_now = load_data(str(i + 1))
    simple_now.load_checkpoint('./checkpoint/simple_' + str(i) + '.ckpt')
    trainer = Trainer(model = simple_now, data_loader = train_dataloader_now, train_times = 200, alpha = 0.5, use_gpu = True,
                      opt_method = "adagrad")
    trainer.run()
    simple_now.save_checkpoint('./checkpoint/simple_' + str(i+1) + '.ckpt')
    simple_now.save_parameters('./parameters/simple_' + str(i+1) + '.json')

    simple_now.load_checkpoint('./checkpoint/simple_' + str(i+1) + '.ckpt')
    tester = Tester(model = simple_now, data_loader = test_dataloader_now, use_gpu = True)
    tester.run_link_prediction(type_constrain = False)

# test the model
# if len(sys.argv) == 2:
#     simple.load_checkpoint('./checkpoint/simple.ckpt')
#     tester = Tester(model = simple, data_loader = test_dataloader, use_gpu = True)
#     tester.run_link_prediction(type_constrain = False)
# elif len(sys.argv) == 3:
#     simple.load_checkpoint('./checkpoint/simple' + sys.argv[1] + '.ckpt')
#     tester = Tester(model = simple, data_loader = test_dataloader, use_gpu = True)
#     tester.run_link_prediction(type_constrain = False)
