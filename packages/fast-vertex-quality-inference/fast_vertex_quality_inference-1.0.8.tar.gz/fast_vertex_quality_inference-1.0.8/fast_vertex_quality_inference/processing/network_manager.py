import fast_vertex_quality_inference.tools.globals as myGlobals
import numpy as np
import pickle
import onnxruntime as ort
import fast_vertex_quality_inference.processing.transformers as tfs
import pandas as pd

# import fast_vertex_quality_inference


class network_manager:

    def __init__(
        self,
        network,
        config,
        transformers,
    ):

        config = pickle.load(open(config, "rb"))

        self.conditions = config["conditions"]
        self.targets = config["targets"]

        # self.Transformers = pickle.load(open(transformers, "rb"))

        transformer_quantiles = pickle.load(open(transformers, "rb"))
        self.Transformers = {}
        for i, (key, quantiles) in enumerate(transformer_quantiles.items()):
            transformer_i = tfs.UpdatedTransformer()
            transformer_i.fit(quantiles, key)
            self.Transformers[key] = transformer_i

        self.branches = self.conditions + self.targets

        if myGlobals._verbose:
            print(f"\n########\nStarting up ONNX InferenceSession for:\n{network}\n")
        self.session = ort.InferenceSession(network)

        # Check model inputs
        self.input_names = [inp.name for inp in self.session.get_inputs()]
        if myGlobals._verbose:
            print(f"\tModel Input Names: {self.input_names}")
        input_shapes = [inp.shape[1] for inp in self.session.get_inputs()]
        if myGlobals._verbose:
            print(f"\tModel Input Dimensions: {input_shapes}")
        for idx, name in enumerate(self.input_names):
            if (
                "latent" in name or "input_vertex_info" in name
            ):  # input_vertex_info from a bug in saving GAN generator?
                self.latent_dim = input_shapes[idx]

        if myGlobals._verbose:
            print("\n")
        # Check model outputs
        self.output_names = [out.name for out in self.session.get_outputs()]
        if myGlobals._verbose:
            print(f"\tModel Output Names: {self.output_names}")
        output_shapes = [out.shape[1] for out in self.session.get_outputs()]
        if myGlobals._verbose:
            print(f"\tModel Output Dimensions: {output_shapes}")
        if myGlobals._verbose:
            print("\n")

        if myGlobals._verbose:
            print(f"\tCondition branches: {self.conditions}\n")
        if myGlobals._verbose:
            print(f"\tTarget branches: {self.targets}")
        if myGlobals._verbose:
            print("\n########\n")

    def query_network(self, inputs, process=True, numpy=False, ignore_targets=False):

        for input_i in inputs:
            try:
                N = np.shape(input_i)[0]
            except:
                pass

        for idx, input_i in enumerate(inputs):
            if isinstance(input_i, str):
                if input_i == "noise":
                    inputs[idx] = np.random.normal(0, 1, (N, self.latent_dim))

        input_data = {}
        for idx, input_i in enumerate(inputs):
            input_data[self.input_names[idx]] = inputs[idx].astype(np.float32)

        output = self.session.run(self.output_names, input_data)[0]

        if not ignore_targets:
            df = {}
            for idx, target in enumerate(self.targets):
                df[target] = output[:, idx]
            output = pd.DataFrame.from_dict(df)

        if process:
            output = tfs.untransform_df(output, self.Transformers)

        if numpy:
            if ignore_targets:
                output = np.asarray(output)
            else:
                output = np.asarray(output[self.targets])

        return output
