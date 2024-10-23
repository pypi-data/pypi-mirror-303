class FakeCache(object):
    action_str = ""
    state_str = "{}"
    index_str = "{}"
    inner_dict = {}

    fake_data = None

    def __init__(self):
        pass

    def get(self, key, default):
        return self.inner_dict.get(key, default)

    def set(self, key, value, ttl):
        self.inner_dict[key] = value

    def delete(self, key):
        print(f'cache delete {key}')
        pass

    def clear(self):
        self.inner_dict.clear()


default_cache = FakeCache()

# action_counter = 0
# state_counter = 0


# def clear():
#     pass
    # global action_counter
    # global state_counter
    # action_counter = 0
    # state_counter = 0


# def query_state():
#     global state_counter
#
#     global_result = {}
#     state = default_cache.fake_data[int(state_counter / 3)]['state']
#     state_counter = state_counter + 1
#     global_result['YCLJS'] = state[0]
#     global_result['BD4R'] = state[1]
#     return global_result
# def query_actions(global_result, alarm_id):
#     utils.dac_facade.query_actions(global_result, alarm_id)
