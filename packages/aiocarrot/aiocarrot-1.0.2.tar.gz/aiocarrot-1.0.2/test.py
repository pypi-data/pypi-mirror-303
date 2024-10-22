from aiocarrot import Carrot, Consumer

from pydantic import BaseModel

import asyncio


class TestModel(BaseModel):
    user_id: int
    amount: float
    is_staff: bool = False


first_consumer = Consumer()

@first_consumer.message(name='test_1')
async def test_1_message(value: int = None) -> None:
    print(('Test value is:', value) if value is not None else 'Empty test value')


second_consumer = Consumer()

@second_consumer.message(name='test_2')
async def test_2_message(value: TestModel) -> None:
    print('Got:', value)


async def send_test_messages(carrot: Carrot) -> None:
    await asyncio.sleep(5)

    await carrot.send('test_1')
    await carrot.send('test_1', value=666)

    await asyncio.sleep(5)

    sample_value = TestModel(
        user_id=5,
        amount=54.35,
    )

    await carrot.send('test_2', value=sample_value)


async def main() -> None:
    consumer = Consumer()
    consumer.include_consumer(first_consumer)
    consumer.include_consumer(second_consumer)

    carrot = Carrot(url='amqp://guest:guest@127.0.0.1:5672/', queue_name='my_test_queue')
    carrot.setup_consumer(consumer)

    asyncio.create_task(send_test_messages(carrot))

    await carrot.run()


if __name__ == '__main__':
    asyncio.run(main())
